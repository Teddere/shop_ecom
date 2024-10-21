from django.db import models
from django.utils.text import slugify

# génération d'image
from io import BytesIO
from PIL import Image
from django.core.files import File

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Catégories'
    @property
    def products(self):
        return Product.objects.filter(category__id=self)

    def __str__(self):
        return str(self.name)
    def get_absolute_url(self):
        return f'/{self.slug}/'
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True,blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    stock = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products/%d/%m/%Y/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='products/%d/%m/%Y/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural= 'Produits'
    def __str__(self):
        return f"{self.name}-({self.stock})"

    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'

    def get_image(self):
        if self.image:
            return f'http://127.0.0.1:8000/{self.image.url}'
        return ''
    def get_thumbnail(self):
        if self.thumbnail:
            return f'http://127.0.0.1:8000/{self.thumbnail.url}'
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()
                return f"http://127.0.0.1:8000/{self.thumbnail.url}"
            else:
                return ""
    def make_thumbnail(self, image,size=(410,600)):
        image = Image.open(image)
        image.convert('RGB')
        image.thumbnail(size)

        thumb_io = BytesIO()
        image.save(thumb_io, format='JPEG', quality=85)
        thumbnail = File(thumb_io, name=image.name)
        return thumbnail

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)




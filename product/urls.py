from django.urls import path,include

from .views import LastProductsList

app_name = 'product'

urlpatterns = [
    path('last-products/', LastProductsList.as_view(), name='last'),
]



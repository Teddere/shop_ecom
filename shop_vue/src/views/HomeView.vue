<template>
  <main>
      <section class="section-banner">
        <Swiper
            :modules="modules"
            :loop="true"
            :autoplay="{
              delay:500,
              disableOnInteraction:false
            }"
            slides-per-view="1"
            :pagination="{ clickable: true }"
            @swiper="onSwiper"
            @slideChange="onSlideChange"
            class="sw-main"
        >
            <swiper-slide class="swiper-slide">
              <div class="sw-image" :style="{'background-image':`linear-gradient(rgba(0,0,0,.6),rgba(0,0,0,.6)),url(${require('@/assets/images/banner_shoe.jpg')})`}">
                <div class="sw-text">
                  <h2>Luxe à Vos Pieds</h2>
                  <p>Élégance inégalée, confort suprême. Découvrez notre collection de chaussures haut de gamme pour un style raffiné.</p>
                  <a href="#">Voir</a>
                </div>
              </div>
            </swiper-slide>
            <swiper-slide class="swiper-slide">
              <div class="sw-image" :style="{'background-image':`linear-gradient(rgba(0,0,0,.6),rgba(0,0,0,.6)),url(${require('@/assets/images/banner-2.jpg')})`}">
                <div class="sw-text">
                  <h2>Élégance Sublime</h2>
                  <p>Raffinement intemporel, luxe à chaque détail. Découvrez notre collection exclusive de vêtements haut de gamme pour un style inégalé.</p>
                  <a href="#" class="btn btn-primary">Voir</a>
                </div>
              </div>
            </swiper-slide>
        </Swiper>
      </section>
      <section class="section-arrival">
        <div class="container-lg">
          <div class="row">
            <div class="col">
              <div class="section-heading">
                <span>Tendance du moment</span>
                <h2>Nouvels arrivages</h2>
              </div>
            </div>
          </div>
          <div class="row">
            <article v-for="product in products" :key="product.id" class="col-sm-6 col-md-4 col-lg-3 mt-2">
              <div class="article-item border p-2 rounded">
                <div class="article-up">
                  <img :src="product.get_thumbnail" alt="">
                  <ul>
                    <li><a href="#"><i class="fa-solid fa-expand"></i></a></li>
                    <li><a href="#"><i class="fa-solid fa-bag-shopping"></i></a></li>
                    <li><a href="#"><i class="fa-solid fa-plus"></i></a></li>
                  </ul>
                </div>
                <div class="article-down">
                  <div class="d-flex align-items-start justify-content-between flex-wrap flex-column">
                    <a href="#" class="article-name">{{product.name}}</a>
                  </div>
                </div>
                <div class="article-detail"><!--Start product detail-->
                  <span class="article-price">{{product.price}} XAF</span>
                </div>
              </div>
            </article>
          </div>
        </div>
      </section>
  </main>
</template>
<script>
  import {Swiper,SwiperSlide} from "swiper/vue";
  import 'swiper/css';
  import 'swiper/css/navigation';
  import 'swiper/css/pagination';

  import { Navigation, Pagination } from 'swiper/modules';
  import axios from "axios";
  export default {
    setup:function (){

      const modules = [Navigation, Pagination]
      const onSwiper = (swiper)=>{ }
      const onSlideChange=()=>{ }

      return {
        modules,onSwiper,onSlideChange
      }
    },
    data:()=>{
      return {
        products:[]
      }
    },
    mounted() {
      this.lastProducts()
    },
    methods: {
      lastProducts() {
        axios.get('/api/v1/last-products/')
            .then(res=>{this.products=res.data})
            .catch(err=>{
              console.log(err)
            })
      }
    },
    components:{
      Swiper,SwiperSlide
    }
  }
</script>
<style scoped lang="scss">
@import "../style/variable";
.section-banner {
  width: 100%;
  height: 74vh;
  // swiper component
  .sw-main {
    width: 100%;
    height: 100%;
    .swiper-slide {
      display: block;
      position: relative;
      overflow: hidden;
      .sw-image {
        width: 100%;
        height: 100%;
        background-clip: border-box;
        background-repeat: no-repeat;
        background-size: cover;
        background-position: center center;
        display: flex;
        justify-content: center;
        align-items: center;
        .sw-text {
          h2 {
            font-size: calc($size + 10px);
            font-style: italic;
            color: var(--bs-white);
            font-weight: 600;
            line-height: 2;
            letter-spacing: -0.02rem;
            text-transform: capitalize;
            text-align: center;
          }
          p {
            font-size: calc($size - 2px);
            font-weight: 400;
            font-style: italic;
            color: rgba(255,255,255,.58);
            text-align: center;
          }
        }
      }
    }
  }
}

.section-arrival {
  padding: 100px 0;
 /****************** 1.3.1 Start Article ********************************/
/* Article up content */
.article-item .article-up {
    display: block;
    position: relative;
    overflow: hidden;
}
/* Article up image content */
.article-item .article-up img {
    width: 100%;
    object-fit: cover;
    object-position: center;
    transition: transform 0.9s ease;
}
/* Article up image content hover*/
.article-item:hover img {
    transform: scale(1.1);
}
/* Article up content label */
.article-up .label {
    position: absolute;
    top: calc(var(--size) - 6px);
    left: calc(var(--size) - 6px);
    display: block;
    padding: 2px 8px;
    text-transform: uppercase;
    font-size: calc(var(--size) - 4px);
    color: var(--white);
    font-weight: 500;
    background: var(--dark);
}
/* Article up content label new */
.article-up .label.new {
    background: var(--bs-success);
}
/* Article up content label sale */
.article-up .label.sale {
    background: var(--bs-danger);
}
/* Article up content  hover */
.article-up .article-hover {
    position: absolute;
    left: 0;
    bottom: 30px;
    text-align: center;
    width: 100%;
}
/* Article up content  hover item */
.article-up .article-hover li {
    position: relative;
    display: inline-block;
    margin-right: calc(var(--size) - 6px);
    top: 100px;
    opacity: 0;
}
.article-up .article-hover li:nth-child(1) {
    transition: all 0.4s ease 0.1s;
}
.article-up .article-hover li:nth-child(2) {
    transition: all 0.4s ease 0.15s;
}
.article-up .article-hover li:nth-child(3) {
    transition: all 0.4s ease 0.2s;
}
.article-up .article-hover li:last-child {
    margin-right: 0;
}
/* article hover link */
.article-up .article-hover li a {
    font-size: 18px;
    color: var(--dark);
    display: block;
    height: 45px;
    width: 45px;
    line-height: 48px;
    text-align: center;
    border-radius: 50%;
    background: var(--white);
    transition: color, background 0.5s ease;
}
.article-up .article-hover li a:hover {
    color: var(--bs-primary);
    background: var(--dark);
}
.article-up .article-hover li a:hover i {
    transform: rotate(360deg);
}

.article-up .article-hover li a i {
    position: relative;
    display: inline-block;
    transform: rotate(0);
    transition: all 0.3s ease;
}
.article-item:hover .article-hover li {
    opacity: 1;
    top: 0;
}
/* Article down */
.article-item .article-down {
    padding-top: calc(var(--size) - 2px);
}
/* Article down detail */
.article-item .article-detail {
    text-align: left;
}
/* Article down detail name */
.article-item .article-name {
    display: block;
    font-size: calc(var(--size) + 5px);
    font-weight: 600;
    color: var(--dark);
    transition: color 0.3s ease;
}
/* Article down detail name hover */
.article-item .article-name:hover {
    color: var(--bs-primary);
}
/* Article down detail price */
.article-item .article-price {
    font-size: calc(var(--size) + 2px);
    font-weight: 600;
    font-style: italic;
    color: var(--bs-primary);
}
/* Article down detail old price */
.article-item .article-old-price {
    font-size: calc(var(--size) - 1px);
    font-style: italic;
    text-decoration: line-through;
    margin-right: 5px;
    color: var(--bs-tertiary-color);
}
/* Article star */
.rating i {
    font-size: calc(var(--size) - 6px);
    margin-right: 1px;
    color: var(--bs-tertiary-color);
}
/* Article last star */
.rating i:last-child {
    margin-right: 0;
}
}

</style>



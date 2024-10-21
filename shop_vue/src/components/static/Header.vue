<template>
  <section class="section-header">
    <nav class="nav-top border border-bottom"><!-- Start nav top-->
      <div class="top-content container-lg h-100 d-flex align-items-center justify-content-center justify-content-sm-between">
        <div class="start d-none d-sm-block">
          Nous contacter&nbsp;:&nbsp;<b>+242 06 838 27 92</b>
        </div>
        <div class="center d-none d-md-block">
          Livraison gratuit à partir de 20 000 XAF d'achat
        </div>
        <div class="end">
          <a href="#"><i class="fa-solid fa-question"></i></a>
          <a href="#"><i class="fa-solid fa-user"></i></a>
          <a href="#"><i class="fa-solid fa-earth-africa"></i></a>
        </div>
      </div>
    </nav><!-- End nav top-->
    <nav class="nav-main container-lg"><!-- start nav main -->
      <div class="main-content d-flex align-items-center justify-content-between">
        <a href="#" class="logo">
          <img src="/assets/logo.png" alt="LOGO-WEBSITE">
        </a>
        <ul id="nav-list" v-bind:class="{'show':showMenu}" class="nav-menu d-md-flex justify-content-md-center align-items-md-center overflow-hidden">
          <li class="menu-item"><a href="#" class="menu-link">Bijoux</a></li>
          <li class="menu-item"><a href="#" class="menu-link">Vêtements</a></li>
          <li class="menu-item"><a href="#" class="menu-link">Lingéries</a></li>
          <li class="menu-item"><a href="#" class="menu-link">Chaussures</a></li>
          <li class="menu-item"><a href="#" class="menu-link">Accessoires</a></li>
          <li class="menu-item"><a href="#" class="menu-link">Contact</a></li>
        </ul>
        <ul class="nav-icons d-flex"><!--Start icon menu -->
          <li class="nav-icon-item position-relative shop-icon">
            <a href="#" class="nav-icons-link">
              <i class="fa-solid fa-shopping-cart"></i>
            </a>
            <div class="label-shp d-flex justify-content-center align-items-center">
              <div class="count-shp">9+</div>
            </div>
          </li>
          <li class="nav-icon-item">
            <a href="#" class="nav-icons-link">
                <i class="fa-solid fa-user"></i>
            </a>
          </li>
          <li class="nav-icon-item">
            <a href="#" class="nav-icons-link">
              <i class="fa-solid fa-search"></i>
            </a>
          </li>
          <li class="nav-icon-btn d-md-none">
            <button id="nav-toggle" type="button" v-on:click="showMenu = !showMenu">
              <i class="fa-solid fa-bars"></i>
            </button>
          </li>
        </ul><!--End icon menu -->
      </div>
    </nav><!--End nav main -->
  </section>
</template>
<style lang="scss">
  @import "./../../style/variable";
  .section-header {
    width: 100%;
    transition: all 0.3s;
    box-shadow: 0 0 3px 0 rgba(0,0,0,0.2);
    // fixed header
    &.fixed-header {
      position: fixed;
      top: 0;
      z-index: 90000;
    }
    // navbar top
    .nav-top {
      background: var(--white);
      height: 40px;

      // left content
      .top-content .start {
        font-size: calc($size - 3px);
        font-style: italic;
        color: $mb-dark;
        margin: calc($size - 10px)  0;
        b {
          font-style: normal;
        }
      }
      // center content
      .top-content .center {
        font-size: calc($size - 3px);
        line-height: 1.8;
        font-style: italic;
        margin: calc($size - 10px) 0;
      }
      // right content
      .top-content .end {
        margin: calc(var(--size) - 12px)  0;
        a {
          font-size: $size;
          line-height: 1.8;
          height: 100%;
          color: $mb-dark;
          padding: 0 calc($size - 8px);
          border-right: 1px solid rgba(0,0,0,.3);
          transition: color .3s ease;
          &:first-child {
            border-left: 1px solid rgba(0,0,0,.3);
          }
          &:hover {
            color: $mb-primary;
          }
        }
      }
    }
    // navbar main
    .nav-main {
      background: var(--white);
      height: 60px;
      .main-content {
        width: 100%;
        height: 100%;
        // logo website
        .logo {
          display: flex;
          align-items: center;
          height: 80%;
          user-select: none;
          img {
            max-width: 100%;
            max-height: 100%;
          }
        }
        // nav icons
        .nav-icons {
          .nav-icon-item {
            margin: 0 calc($size - 8px);
            &:first-child {
              margin-left: 0;
            }
            .nav-icons-link {
              color: $mb-dark;
              font-size: calc($size + 2px);
              transition: color .3s ease;
              &:hover {
                color: $mb-primary;
              }
            }
            &.shop-icon .label-shp {
                position: absolute;
                top: 13px;
                left: -8px;
                width: 15px;
                height: 15px;
                display: block;
                .count-shp {
                  width: 100%;
                  height: 100%;
                  padding: 0 1.2px ;
                  font-size: calc($size - 6px);
                  font-style: italic;
                  font-weight: 600;
                  border-radius: 50%;
                  color: var(--bs-white);
                  background: $mb-primary;
                }
            }
          }
          .nav-icon-btn {
            #nav-toggle {
              display: inline-block;
              padding: calc($size - 13px) calc($size - 8px);
              border-radius: 5px;
              border: 1.5px solid $mb-dark;
              color: $mb-dark;
              background: var(--bs-white);
              transition: color,border, background 0.3s ease;
              &:hover {
                color: var(--bs-white);
                border-color: var(--bs-white) ;
                background: $mb-primary;
              }
            }
          }
        }
        // nav list
        .nav-menu {
          display: block;
          position: absolute;
          top: 100px;
          left: 0;
          right: 0;
          z-index: 9;
          height: 0;
          background: var(--bs-white);
          transition: height 600ms ease;
          &.show {
            height: 233px;
          }
          .menu-item {
            display: block;
            text-align: center;
            border-bottom: 1px solid $mb-gray;
            &:first-child {
              border-top: 1px solid $mb-gray;
            }
            .menu-link {
              display: inline-block;
              padding: 6px 0;
              width: 100%;
              height: 100%;
              line-height: 1.6;
              font-weight: 600;
              text-transform: capitalize;
              color: $mb-dark;
              transition: color,background .3s ease;
              &:hover {
                color: $mb-primary;
                background: rgba(170,68,22,0.1);
              }
            }
          }
        }
      }
    }
    @media (min-width: 768px) {
      .nav-main .main-content {
        .nav-menu {
          position: static;
          height: auto;
          .menu-item {
            border: none;
            margin: 0 calc($size - 6px);
            &:first-child {
              border: none;
              margin-left: 0;
            }
            .menu-link {
              width: auto;
              height: auto;
              padding: 0;
              &:hover {
                background: transparent;
              }
            }
          }
        }
      }
    }
  }
</style>
<script>
export default {
  data:function(){
    return {
      showMenu:false
    }
  },
}
</script>
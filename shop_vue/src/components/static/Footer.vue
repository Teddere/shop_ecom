<template>
  <section class="section-service">
    <div class="container-lg">
      <div class="row">
        <div class="col-sm-6 col-md-4 col-lg-3"><!-- start service item -->
          <div class="service-item">
            <i class="fa-solid fa-shopping-cart"></i>
            <h6>Livraison gratuite</h6>
            <p>Pour toute commande supérieure à 100.000 Fcfa</p>
          </div>
        </div><!-- End service item -->
        <div class="col-sm-6 col-md-4 col-lg-3"><!-- Start service item -->
          <div class="service-item">
            <i class="fa-solid fa-money-bill"></i>
            <h6>Livraison gratuite</h6>
            <p>Tous nos produits sont garanties 1 an</p>
          </div>
        </div><!-- End service item -->
        <div class="col-sm-6 col-md-4 col-lg-3"><!-- Start service item -->
          <div class="service-item">
            <i class="fa-solid fa-phone"></i>
            <h6>Assistance 24h/24</h6>
            <p>Unique sur notre support</p>
          </div>
        </div><!-- end service item -->
        <div class="col-sm-6 col-md-4 col-lg-3"><!-- Start service item -->
          <div class="service-item">
            <i class="fa-solid fa-lock"></i>
            <h6>Payment sécurisé</h6>
            <p>100% protection</p>
          </div>
        </div><!--End service item -->
      </div>
    </div>
  </section>
  <section class="section-footer">
    <div class="container-lg">
      <div class="row">
        <div class="col-12">
          <div class="footer-copyright">
            <p>Copyright &copy; {{date}} | Tous droits réservés</p>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref} from "vue";

const date=ref(new Date().getFullYear())
</script>

<style lang="scss">
  @import "./../../style/variable";
  .section-service {
    padding-top: 50px;
    padding-bottom: 50px;
    .service-item {
      position: relative;
      padding-left: 65px;
      margin-bottom: 20px;
      i {
        position: absolute;
        left: 0;
        top: 4px;
        font-size: 36px;
        color: $mb-primary;
      }
      h6 {
        color: $mb-dark;
        font-weight: 600;
        margin-bottom: 5px;
      }
      p {
        margin-bottom: 0;
      }
    }
  }
  .section-footer {
    padding-top: 45px;
    .footer-copyright {
      border-top: 1px solid #e1e1e1;
      padding: 18px 0 25px;
      text-align: center;
    }
  }
</style>
<template>
  <Header />
  <router-view/>

</template>

<style lang="scss">
  @import "./style/style";
  @import "~@fortawesome/fontawesome-free/css/all.min.css";
</style>
<script setup >
  import Header from '@/components/static/Header.vue';
  import Footer from "@/components/static/Footer.vue";
</script>
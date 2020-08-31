<template>
  <div id="app">
    <NavBar />
    <router-view />
    <footer class="page-footer text-center mt-auto">
      <hr>
      &lt; 
      - - -  
      Copyright © 2020 
      - - -
      &gt;
    </footer>
  </div>
</template>

<script>
import NavBar from '@/components/NavBar.vue'
export default {
  name: 'App',
  components: {
    NavBar
  }
};
</script>

<style lang="scss">
	@import '/css/darkly.bootstrap.min.css';
</style>
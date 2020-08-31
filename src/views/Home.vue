<template>
  <b-container>
    <Header />
    <b-row>
      <b-col fluid>
        <h2>
          App Title
        </h2>
        <p>
          Get things done.
        </p>
      </b-col>
    </b-row>
    <b-row>
      <b-col fluid>
        <router-link 
          class="btn btn-lg btn-block btn-success"
          to="/register"
        >
          REGISTER
        </router-link>
      
        <hr>
        <router-link 
          class="btn btn-lg btn-block btn-info"
          to="/login"
        >
          LOGIN
        </router-link>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import Header from '@/components/Header.vue'
export default {
  name: 'Home',
  components: {
    Header
  },
  data() {
    return {}
  },
  methods: {}
}
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>

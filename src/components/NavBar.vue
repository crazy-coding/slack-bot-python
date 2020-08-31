<template>
  <b-navbar
    toggleable="lg"
    type="faded"
    variant="secondary"
  >
    <b-navbar-brand href="/">
      App Title
    </b-navbar-brand>

    <!-- Right aligned nav items -->
    <b-navbar-nav
      class="ml-auto"
    >
      <b-button
        size="sm" 
        class="btn-warning my-2 my-sm-0" 
        to="/"
        type="button"
      >
        Logout
      </b-button>
      <b-button
        size="sm" 
        class="btn-info my-2 my-sm-0" 
        to="/login"
        type="button"
      >
        Login
      </b-button>
    </b-navbar-nav>
  </b-navbar>
</template>


<script>
export default {
	name: 'NavBar'
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.navbar-nav a.btn {
	margin-left: 15px;
	display: block;
}
</style>
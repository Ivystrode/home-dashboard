<template>
  <v-app>
    <v-main>
      <div class="main-container">
        <Header title="Dashboard"/>
        <router-view/>  
      </div>
        <Footer/>   
    </v-main>
  </v-app>
</template>


<script>
import Header from './components/Header'
import Footer from './components/Footer'

export default {
  name: 'App',
  components: {
    Header,
    Footer
  },

  data: () => ({
    //
  }),
}
</script>

<style>
.main-container {
  height: 100%;
  min-height: 100%;
  padding-bottom: 20vh;
  /* background-color: #2e344d; */
  background: linear-gradient(110deg, #2e344d, #071344);
}
</style>
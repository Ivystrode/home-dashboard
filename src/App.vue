<template>
  <v-app>
    <v-main>
      <!-- header -->
      <Header title="Dashboard"/>
      <router-view/>
      <Footer/>
      <!-- footer -->
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

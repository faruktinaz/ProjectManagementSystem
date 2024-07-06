<template>
  <v-app>
    <v-main>
      <Home />
    </v-main>
  </v-app>
</template>

<script>
import Home from './components/HomePage.vue'

export default {
  name: 'App',

  components: {
    Home
  },

  data: () => ({
    //
  }),
}
</script>

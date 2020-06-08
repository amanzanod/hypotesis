<template>

  <div id="app">
    <div v-if="$route.path.includes('/login')">
      <router-view/>
    </div>
    <MainMenuApp v-else />
    <div v-if="$route.path.includes('/login')"></div>
    <div id="main_container" v-else>
      <HeaderApp/>
      <ContentApp/>
      <FooterApp/>
    </div>
  </div>

</template>

<script>

  import MainMenuApp from './layouts/MainMenu.vue';
  import HeaderApp from './layouts/Header.vue';
  import ContentApp from './layouts/Content.vue';
  import FooterApp from './layouts/Footer.vue';

  export default {
    name: 'app',
    components: {
      MainMenuApp, HeaderApp, ContentApp, FooterApp
    }
  }

</script>

<style lang="scss">

  @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300&display=swap');
  @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@600&display=swap');
  @import url('https://fonts.googleapis.com/css2?family=Varela+Round&display=swap');

  body {
    height: 100%;
    margin: 0;
  }

  #app {
    font-family: 'Montserrat', sans-serif;;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    display: flex;
    height: 100vh;
    #main_container {
      width: 100%;
      height: 100vh;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }

  }
</style>

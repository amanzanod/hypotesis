<template>

  <div id="router-view">
      <ContainerHeaderApp v-bind:num="contexts" v-bind:title="title" v-bind:list="true"/>
      <div class="container-view">
      </div>
  </div>

</template>

<script>

    import ContainerHeaderApp from '@/layouts/ContainerHeader.vue';

    export default {
        name: 'Admin',
        components: {
            ContainerHeaderApp
        },
        data() {
            return {
                title: 'Administración',
                contexts: 0,
            }
        },
    }

</script>

<style lang="scss">

    #router-view {
        .container-view {
            background-color: white;
            border: 1px solid #DFDFDF;
            padding: 30px;


        }
    }
</style>

<template>

  <div id="router-view">
      <ContainerHeaderApp v-bind:num="contexts" v-bind:title="title" v-bind:list="false" v-bind:create_href="create_href"/>
      <div class="container-view">
      </div>
  </div>

</template>

<script>

    import ContainerHeaderApp from '@/layouts/ContainerHeader.vue';

    export default {
        name: 'SchoolForum',
        components: {
            ContainerHeaderApp
        },
        data() {
            return {
                title: 'Foro',
                create_href: '',
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

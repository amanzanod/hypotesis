<template>

    <router-link v-if="num===1" class="relation" :to="href">
        {{ num }} usuario
    </router-link>
    <router-link v-else class="relation" :to="href">
        {{ num }} usuarios
    </router-link>

</template>

<script>

    import {HYP_MANAGER_ROLE} from '../../api/constants';

    export default {
        name: 'LinkTable',
        props: {
            href: Object,
            item: Object
        },
        data() {
            return {
                num: '0'
            }
        },
        beforeMount () {

            this.axios
                .get( HYP_MANAGER_ROLE + this.item.alias + '/users/?format=json')
                .then(response => {
                    this.num = response.data.length;
                });
        },
    }

</script>

<style scoped lang="scss">

    a{
        color: #64A5AF;
        font-weight: 600;
        &.relation {
            border: 1px solid #64A5AF;
            border-radius: 10px;
            padding: 4px 10px;
            &:hover {
                text-decoration: none;
                background-color: #64A5AF;
                color: white !important;
            }
        }
    }


</style>

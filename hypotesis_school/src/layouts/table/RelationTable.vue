<template>

    <router-link class="relation" :to="{ name: 'Course', params: { alias: course }}">
        {{ name }}
    </router-link>

</template>

<script>

    import {HYP_CONTEXT_COURSE} from '../../api/constants';

    export default {
        name: 'LinkTable',
        props: {
            course: String
        },
        data() {
            return {
                name: '',
                alias: ''
            }
        },
        beforeMount () {

            this.axios
                .get( HYP_CONTEXT_COURSE + this.course+ '/?format=json')
                .then(response => {
                    this.name = response.data.name;
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

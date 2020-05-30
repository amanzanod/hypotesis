<template>

    <div class="container-header">
        <h1 class="title_container">{{ title }} <span>({{ num }})</span></h1>
        <router-link v-if="list" to="Users" class="create_entity">
            <i class="fas fa-plus"></i>
            <div class="triangle-form"></div>
        </router-link>
    </div>
</template>

<script>

    export default {
        name: 'ContainerHeader',
        props: {
            num: String,
            title: String,
            list: Boolean
        }
    }

</script>

<style scoped lang="scss">

    .container-header {
        background-color: #F6F6F6;
        border: 1px solid #DFDFDF;
        height: 105px;
        text-align: left;
        display: flex;
        align-items: center;
        padding: 0 50px;
        h1.title_container {
            font-family: 'Montserrat', sans-serif;
            font-size: 25px;
            font-weight: 600;
            margin-bottom: 0;
            color: #727475;
            span {
                font-weight: 300;
            }
        }
        .create_entity {
            width: 68px;
            height: 54px;
            background-color: #64a5af;
            display: flex;
            align-items: center;
            position: absolute;
            justify-content: center;
            border-radius: 10px 0 0 10px;
            font-size: 20px;
            right: 27px;
            padding: 0 0 0 8px;
            &:hover {
                text-decoration: none;
                background-color: #7ccbd7;
            }
            i.fas {
                color: white;
            }
            .triangle-form {
                width: 0;
                height: 0;
                border-right: 5px solid transparent;
                border-top: 5px solid #527d84;
                border-left: 5px solid #527d84;
                border-bottom: 5px solid transparent;
                position: relative;
                top: 32px;
                left: 16px;
            }

        }
    }

</style>

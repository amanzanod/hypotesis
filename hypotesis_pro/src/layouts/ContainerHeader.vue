<template>

    <div class="container-header">
        <h1 class="title_container">{{ title }} <span>({{ num }})</span></h1>
    </div>

</template>

<script>

    export default {
        name: 'ContainerHeader',
        props: {
            num: Number,
            title: String
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
    }

</style>

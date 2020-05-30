<template>
    <div id="content">
        <div class="hyp_container">
            <router-view/>
        </div>
    </div>
</template>

<script>


</script>

<style scoped lang="scss">

    #content {
        background-color: #CECECE;
        height: 100%;
        z-index: 0;
        padding: 30px;
        overflow-y: scroll;
        &::-webkit-scrollbar-track {
            -webkit-box-shadow: inset 0 0 6px rgba(190, 190, 190, 0.3);
            border-radius: 0;
            background-color: #F5F5F5;
        }
        &::-webkit-scrollbar {
            width: 6px;
            background-color: #F5F5F5;
        }
        &::-webkit-scrollbar-thumb{
            border-radius: 0;
            -webkit-box-shadow: inset 0 0 6px rgba(206, 206, 206, 0.6);
            background-color: #4C7E86;
        }
        .hyp_container {
            background-color: white;
            border: 1px solid #DFDFDF;
        }
    }

</style>

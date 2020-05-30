<template>
    <footer id="footer">
        <div class="grey_stripe left"></div>
        <span class="title_footer">
          © 2020 - Hypotesis PRO • Antonio Manzano Díaz • TFG Grado Multimedia • <span class="underline">Política de Privacidad y Política de Cookies</span>
        </span>
        <div class="grey_stripe right"></div>
    </footer>
</template>

<script>

</script>

<style scoped lang="scss">

    #footer {
        height: 66px;
        min-height: 66px;
        background-color: #F7F7F7;
        color: #64A5AF;
        -webkit-box-shadow: 0 0 5px 6px rgba(0,0,0,0.31);
        -moz-box-shadow: 0 0 5px 6px rgba(0,0,0,0.31);
        box-shadow: 0 0 5px 6px rgba(0,0,0,0.31);
        width: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 1;
        position: relative;
        .title_footer {
            font-family: "Varela Round", sans-serif;
            font-size: 15px;
            color: #373737;
            .underline {
                text-decoration: underline;
                cursor: pointer;
                &:hover {
                    color: #4C7E86;
                }
            }
        }
        .grey_stripe {
            background-color: #e0e0e0;
            width: 14px;
            height: 66px;
            position: absolute;
            &.left {
                left: 0;
            }
            &.right {
                right: 0;
            }
        }
    }

</style>

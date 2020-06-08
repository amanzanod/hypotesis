<template>
    <main id="main" class="container_404">
        <h2>Página no encontrada</h2>
        <span class="error_404">404</span>
        <div class="error_img"></div>
        <p class="error_p">Lo sentimos, no hemos podido encontrar la página que buscas.</p>
        <p class="error_p"><a class="btn_back" href="./">Ir al inicio</a></p>
    </main>
</template>
<style lang="scss">
    #main {
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 100px;
        h2 {
            text-align: center;
            color: #4f828a;
        }
        span.error_404 {
            text-align: center;
            font-size: 149px;
            font-weight: bold;
            color: #64a5af;
            @media (max-width: 576px) {
                font-size: 89px;
            }
        }
        p.error_p {
            text-align: center;
            margin: 10px 10px 40px;
            color: #4f828a;
            a.btn_back {
                background-color: #64a5af;
                text-decoration: none;
                color: white;
                padding: 6px 12px;
                border-radius: 10px;
                &:hover {
                    background-color: #7cc8d3;
                }
            }
        }
        div.error_img {
            height: 105px;
            width: 400px;
            background-image: url('../assets/images/error.svg');
            background-repeat: no-repeat;
            margin: 10px 0;
            background-position: 50%;
            @media (max-width: 576px) {
                height: 70px;
                width: 80%;
            }
        }
    }

</style>

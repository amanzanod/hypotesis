<template>
    <header id="header">
        <div class="grey_stripe left"></div>
        <div class="hyp_breadcrumb">
            <router-link class="link_breadcrumb" to="/">
                <span class="home_button"><i class="fas fa-home"></i></span>
            </router-link>
            <router-link class="link_breadcrumb" to="/">
                <span class="home_text">Inicio</span>
            </router-link>
            <span class="actual">{{ currentRouteName }}</span>
        </div>
        <div class="action_header">
            <label class="label-search">
                <input class="btn-search" type="search" placeholder="Buscar">
            </label>
            <label class="label-language">
                <i class="fas fa-globe-europe"></i>
                ESP
            </label>
            <label class="label-config">
                <i class="fas fa-cog"></i>
            </label>
            <router-link class="link_logout" to="/login">
                <label class="label-logout">
                    <i class="fas fa-sign-out-alt"></i>
                </label>
            </router-link>
        </div>
        <div class="grey_stripe right"></div>
    </header>
</template>

<script>

    export default {
        name: 'Header',
        computed: {
            currentRouteName() {
                return this.$route.meta ? null : this.$route.meta;
            }
        }
    }


</script>


<style scoped lang="scss">

    #header {
        height: 66px;
        min-height: 66px;
        background-color: #F7F7F7;
        color: #64A5AF;
        -webkit-box-shadow: 0 0 5px 6px rgba(0,0,0,0.31);
        -moz-box-shadow: 0 0 5px 6px rgba(0,0,0,0.31);
        box-shadow: 0 0 5px 6px rgba(0,0,0,0.31);
        z-index: 1;
        position: relative;
        display: flex;
        padding: 0 36px;
        align-items: center;
        justify-content: space-between;
        .hyp_breadcrumb {
            font-family: "Varela Round", sans-serif;
            font-size: 15px;
            color: #64A5AF;
            a.link_breadcrumb {
                color: inherit;
                &:hover {
                    text-decoration: none;
                }
            }
            .home_button {
                font-size: 26px;
                padding-right: 20px;
                cursor: pointer;
                &:hover {
                    color: #3f6d75;
                }
            }
            .home_text {
                padding-right: 12px;
                cursor: pointer;
                font-weight: 600;
                position: relative;
                top: -3px;
                &:hover {
                    color: #3f6d75;
                }
                &::after {
                    font-family: FontAwesome, serif;
                    content: "\f054";
                    padding-left: 12px;
                    top: 1px;
                    position: relative;
                    color: #727475;
                    cursor: inherit;
                    font-weight: 300;
                }
            }
            .actual {
                color: #727475;
                position: relative;
                top: -3px;
            }
        }
        .action_header {
            display: flex;
            .label-search {
                width: 330px;
                margin-right: 10px;
                input.btn-search {
                    height: 47px;
                    padding: 0 16px;
                    min-width: 17rem;
                    width: 100%;
                    color: #D2CFCF !important;
                    text-align: left;
                    cursor: initial;
                    border: 1px solid #DFDFDF;
                    font-size: 18px;
                    background-color: white;
                    font-family: 'Montserrat', sans-serif;
                    &:focus {
                        border: inherit;
                    }
                }
            }
            .label-language {
                height: 45px;
                width: 86px;
                border: 1px solid #DFDFDF;
                margin-right: 10px;
                background-color: white;
                display: flex;
                align-items: center;
                justify-content: center;
                >.fas {
                    font-size: 22px;
                    margin-right: 7px;
                }
            }
            .label-config {
                height: 45px;
                width: 86px;
                border: 1px solid #DFDFDF;
                margin-right: 15px;
                background-color: white;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 27px;
                color: #CECECE;
            }
            a.link_logout {
                color: inherit;
                text-decoration: none;
                cursor: pointer;
            }
            .label-logout {
                height: 45px;
                display: flex;
                align-items: center;
                margin-right: 12px;
                cursor: pointer;
                .fas {
                    font-size: 35px;
                }
            }
            i.fa.fa-search {
                position: relative;
                left: -29px;
                color: #3772b4;
                cursor: pointer;
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

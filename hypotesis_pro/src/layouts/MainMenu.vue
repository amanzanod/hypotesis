<template>
    <div id="main_menu">
        <div id="main_menu_header">
            <img id="logo_main" src="../assets/hypotesis_logo.svg"  alt="Hypotesis PRO"/>
            <div class="user_name">{{ name }} {{surname1}}</div>
            <div class="collapse_button"><i class="fas fa-angle-left"></i></div>
        </div>
        <div id="main_menu_content">
            <div class="user_username">{{ username }}</div>
            <div class="user_role_name">{{ role }}</div>
            <nav id="menu">
                <ul class="menu_buttons">
                    <li class="menu_button current">
                        <router-link :to="{ name: 'Users'}">
                            <i class="fas fa-users"></i>
                            <span class="button_text">Usuarios</span>
                        </router-link>
                    </li>
                    <li class="menu_button">
                        <router-link :to="{ name: 'Roles'}">
                            <i class='fas fa-suitcase-rolling'></i>
                            <span class="button_text tab1">Roles</span>
                        </router-link>
                    </li>
                    <li class="menu_button">
                        <router-link :to="{ name: 'Permissions'}">
                            <i class="fas fa-hammer"></i>
                            <span class="button_text tab1">Permisos</span>
                        </router-link>
                    </li>
                    <li class="menu_button">
                        <router-link :to="{ name: 'Contexts'}">
                            <i class="fas fa-globe"></i>
                            <span class="button_text">Contextos</span>
                        </router-link>
                    </li>
                    <li class="menu_button">
                        <router-link :to="{ name: 'Grades'}">
                            <i class="fas fa-graduation-cap"></i>
                            <span class="button_text tab1">Grados</span>
                        </router-link>
                    </li>
                    <li class="menu_button">
                        <router-link :to="{ name: 'Masters'}">
                        <i class="fas fa-medal"></i>
                        <span class="button_text tab1">Máster</span>
                        </router-link>
                    </li>
                    <li class="menu_button">
                        <router-link :to="{ name: 'Courses'}">
                        <i class="fas fa-book"></i>
                        <span class="button_text tab1">Cursos</span>
                        </router-link>
                    </li>
                    <li class="menu_button">
                        <router-link :to="{ name: 'Classrooms'}">
                        <i class="fas fa-chalkboard"></i>
                        <span class="button_text tab1">Aulas</span>
                        </router-link>
                    </li>
                    <li class="menu_button">
                        <router-link :to="{ name: 'Categories'}">
                        <i class="fas fa-copy"></i>
                        <span class="button_text tab1">Categorías</span>
                        </router-link>
                    </li>
                    <li class="menu_button">
                        <router-link :to="{ name: 'Notifications'}">
                        <i class="fas fa-bell"></i>
                        <span class="button_text">Notificaciones</span>
                        </router-link>
                    </li>
                    <li class="menu_button">
                        <router-link :to="{ name: 'Forum'}">
                        <i class="fas fa-comments"></i>
                        <span class="button_text">Foro</span>
                        </router-link>
                    </li>
                    <li class="menu_button">
                        <router-link :to="{ name: 'News'}">
                        <i class="fas fa-newspaper"></i>
                        <span class="button_text">Tablón Anuncios</span>
                        </router-link>
                    </li>
                    <li class="menu_button">
                        <router-link :to="{ name: 'Reports'}">
                        <i class="fas fa-chart-line"></i>
                        <span class="button_text">Informes</span>
                        </router-link>
                    </li>
                    <li class="menu_button">
                        <router-link :to="{ name: 'Admin'}">
                        <i class="fas fa-cogs"></i>
                        <span class="button_text">Administración</span>
                        </router-link>
                    </li>
                </ul>
            </nav>
        </div>
        <div class="white_stripe"></div>
    </div>
</template>

<script>

    import {HYP_MANAGER_USER} from '../api/constants';

    export default {
        name: 'MainMenu',
        data () {
            return {
                name: null,
                surname1: null,
                username: null,
                role: null
            }
        },
        components: {},
        props: [],
        computed: {

        },
        methods: {
        },
        beforeCreate () {
            this.user = 'amanzanod';
        },
        beforeMount () {
            this.axios
                .get( HYP_MANAGER_USER + this.user + '/?format=json')
                .then(response => {
                    const data = response.data;
                    this.name = data.name;
                    this.surname1 = data.surname1;
                    this.username = data.username;
                    this.role = data.role.name;
                })
        }
    }

</script>


<style scoped lang="scss">

    #main_menu {
        background-color: #1A5A64;
        color: white;
        width: 280px;
        min-width: 280px;
        position: relative;
        z-index: 3;
        #main_menu_header {
            height: 218px;
            display: flex;
            padding-right: 14px;
            flex-direction: column;
            justify-content: space-between;
            background: rgb(13,45,50);
            background: linear-gradient(0deg, rgba(13,45,50,1) 0%, rgba(26,90,100,1) 100%);
            #logo_main {
                margin: 18px;
            }
            .user_name {
                margin: 7px;
            }
            .collapse_button {
                position: absolute;
                right: 25px;
                top: 11px;
                font-size: 38px;
                color: #373737;
                cursor: pointer;
                &:hover{
                    color: #4C7E86;
                }
            }
        }
        #main_menu_content {
            padding: 0;
            padding-right: 14px;
            border-top: 1px solid #2e4f54;
            background: rgb(13,45,50);
            background: linear-gradient(180deg, rgba(13,45,50,1) 0%, rgba(26,90,100,1) 100%);
            .user_username {
                font-size: 15px;
                color: #A7A7A7;
                margin: 5px;
            }
            .user_role_name {
                font-family: "Varela Round", sans-serif;
                font-size: 17px;
                color: #4C7E86;
                margin: 15px 5px;
            }
            nav#menu {
                ul.menu_buttons {
                    list-style: none;
                    padding: 5px 0;
                    text-align: left;
                    margin: 40px 0 0 0;
                    li.menu_button {
                        >a {
                            cursor: pointer;
                            display: flex;
                            align-items: center;
                            height: 34px;
                            font-family: "Varela Round", sans-serif;
                            font-size: 16px;
                            position: relative;
                            color: white;
                            &:hover {
                                outline: none;
                                text-decoration: none;
                            }
                            i.fas {
                                width: 23px;
                                min-width: 23px;
                                margin: 0 15px;
                                text-align: center;
                            }
                            span.button_text {
                                padding-left: 5px;
                                &.tab1 {
                                    padding-left: 17px;
                                }
                            }
                            &:hover {
                                background-color: #4C7E86;
                            }
                            &.router-link-exact-active {
                                background-color: #082226;
                                color: #4C7E86;
                                &::after {
                                    content: " ";
                                    height: 34px;
                                    width: 14px;
                                    position: absolute;
                                    right: -14px;
                                    background-color: #4C7E86;
                                }
                            }
                        }
                    }
                }
            }
        }
        .white_stripe {
            background-color: #ffffff21;
            height: 100%;
            position: absolute;
            width: 14px;
            top: 0;
            right: 0;
        }

    }

</style>

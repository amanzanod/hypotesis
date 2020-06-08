<template>
    <div id="main_menu" :class="{'collapsed': is_collapsed}">
        <div id="main_menu_header">
            <img id="logo_main" src="../assets/logo_horizontal.svg"  alt="Hypotesis Code"/>
            <div class="user_name">{{ name }} {{surname1}}</div>
            <div class="user_username">{{ username }}</div>
            <div class="collapse_button" ><i class="fas fa-angle-left"></i></div>
        </div>
        <div id="main_menu_content">
            <div class="picture_user">
                <b-img class="picture_img" :src="picture"></b-img>
            </div>
            <nav id="menu">
                <div v-if="course" class="label_menu">CURSO</div>
                <ul  v-if="course" class="menu_buttons">
                    <li class="menu_button current">
                        <router-link :to="{ name: 'CourseStart'}">
                            <i class="fas fa-door-open"></i>
                            <span class="button_text">Portada</span>
                        </router-link>
                    </li>
                    <li class="menu_button">
                        <router-link :to="{ name: 'CourseNews'}">
                            <i class="fas fa-rss"></i>
                            <span class="button_text">Tablón</span>
                        </router-link>
                    </li>
                    <li class="menu_button">
                        <router-link :to="{ name: 'CourseCompetences'}">
                            <i class="fas fa-medal"></i>
                            <span class="button_text">Competencias</span>
                        </router-link>
                    </li>
                    <li class="menu_button">
                        <router-link :to="{ name: 'CourseUsers'}">
                            <i class="fas fa-users"></i>
                            <span class="button_text">Participantes</span>
                        </router-link>
                    </li>
                    <li class="menu_button">
                        <router-link :to="{ name: 'CourseItinerary'}">
                            <i class="fas fa-map-signs"></i>
                            <span class="button_text">Itinerario</span>
                        </router-link>
                    </li>
                    <li class="menu_button">
                        <router-link :to="{ name: 'CourseForum'}">
                            <i class="fas fa-comments"></i>
                        <span class="button_text">Foro</span>
                        </router-link>
                    </li>
                </ul>
                <div v-else class="space-no-course"></div>
                <div class="label_menu">ESTUDIANTE</div>
                <ul class="menu_buttons">
                    <li class="menu_button current">
                        <router-link :to="{ name: 'UserProfile'}">
                            <i class="fas fa-user"></i>
                            <span class="button_text">Perfil</span>
                        </router-link>
                    </li>
                    <li class="menu_button">
                        <router-link :to="{ name: 'UserCourses'}">
                            <i class="fas fa-book"></i>
                            <span class="button_text">Mis Cursos</span>
                        </router-link>
                    </li>
                    <li class="menu_button">
                        <router-link :to="{ name: 'UserSchedule'}">
                            <i class="fas fa-calendar-alt"></i>
                            <span class="button_text">Calendario</span>
                        </router-link>
                    </li>
                    <li class="menu_button">
                        <router-link :to="{ name: 'UserNotifications'}">
                            <i class="fas fa-bell"></i>
                            <span class="button_text">Notificaciones</span>
                        </router-link>
                    </li>
                </ul>
                <div class="label_menu">ESCUELA</div>
                <ul class="menu_buttons">
                    <li class="menu_button current">
                        <router-link :to="{ name: 'SchoolCourses'}">
                            <i class="fas fa-graduation-cap"></i>
                            <span class="button_text">Oferta Cursos</span>
                        </router-link>
                    </li>
                    <li class="menu_button">
                        <router-link :to="{ name: 'SchoolNews'}">
                            <i class="fas fa-newspaper"></i>
                            <span class="button_text">Noticias</span>
                        </router-link>
                    </li>
                    <li class="menu_button">
                        <router-link :to="{ name: 'SchoolForum'}">
                            <i class="fas fa-comments"></i>
                            <span class="button_text">Foro</span>
                        </router-link>
                    </li>
                    <li class="menu_button">
                        <router-link :to="{ name: 'SchoolAdmin'}">
                            <i class="fas fa-tasks"></i>
                            <span class="button_text">Trámites</span>
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
                role: null,
                picture: null,
                is_collapsed: false,
                course: null,
            }
        },
        components: {},
        props: [],
        methods: {
            collapsed() {
                this.$menu.collapsed = true;
                this.is_collapsed = true;
            }
        },
        beforeCreate () {
            this.is_collapsed = this.$menu.collapsed;
            this.user = localStorage.getItem("username");

            if (this.user === 'false') {
                this.$router.replace({ name: 'Login'});
            } else if (this.user === null) {
                this.$router.replace({ name: 'Login'});
            }

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
                    this.picture = data.picture;
                })
        }
    }

</script>


<style scoped lang="scss">

    #main_menu {
        background-color: #373737;
        color: white;
        width: 280px;
        min-width: 280px;
        position: relative;
        z-index: 3;
        height: 100%;
        &.collapsed {
            width: 100px;
            min-width: 100px;
        }
        #main_menu_header {
            height: 180px;
            display: flex;
            padding-right: 14px;
            flex-direction: column;
            justify-content: space-between;
            background: #64A5AF;
            position: relative;
            #logo_main {
                margin: 18px 29px 0 0;
            }
            .user_name {
                margin: 7px;
                position: relative;
                top: -14px;
            }
            .user_username {
                font-size: 15px;
                color: #373737;
                margin: 5px;
                position: relative;
                top: -55px;
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
            background: #373737;
            position: relative;
            .user_role_name {
                font-family: "Varela Round", sans-serif;
                font-size: 17px;
                color: #4C7E86;
                margin: 15px 5px;
            }
            .picture_user {
                width: 120px;
                height: 120px;
                overflow: hidden;
                border-radius: 60px;
                border: 9px solid #64A5AF;
                position: relative;
                left: 73px;
                top: -65px;
                .picture_img {
                    height: 100%;
                }
            }
            .space-no-course {
                height: 40px;
            }
            nav#menu {
                position: relative;
                top: -52px;
                .label_menu{
                    font-family: "Varela Round", sans-serif;
                    font-size: 18px;
                    color: #A5A5A5;
                    text-align: left;
                    margin-left: 17px;
                }
                ul.menu_buttons {
                    list-style: none;
                    padding: 5px 0;
                    text-align: left;
                    margin: 0 0 0 0;
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
                                background-color: #222;
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

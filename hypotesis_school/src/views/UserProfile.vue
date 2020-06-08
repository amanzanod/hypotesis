<template>

  <div id="router-view">
      <div class="container-header">

          <div class="header-profile">
              <div class="data-left">
                  <div class="left-top">
                      <i class="fas fa-map-marker-alt"></i>
                      <span>{{ user.province.name }} ({{ user.country.name }})</span>
                  </div>
                  <div class="left-bottom">
                      <i class="fas fa-book"></i>
                      <span>{{ user.role.name }} desde {{ user.since }}</span>
                  </div>
              </div>
              <div class="data-center">
                  <div class="picture_user">
                      <b-img class="picture_img" :src="user.picture"></b-img>
                  </div>
                  <div class="user-name">{{ user.name }} {{ user.surname1 }} {{ user.surname2}}</div>
                  <div class="user-title">{{ user.title }}</div>
              </div>
              <div class="data-right">
                  <span>{{ user.email }}</span><i class="fas fa-at"></i>
              </div>
          </div>


          <div class="create_entity">
              <i class="fas fa-plus"></i>
              <div class="triangle-form"></div>
          </div>

      </div>
      <div class="container-view">

          <div class="info">
              <div class="description">
                  <h3 class="label-info">Acerca de mí</h3>
                  <div class="aboutme" v-html="user.about_me">
                      {{ user.about_me }}
                  </div>
              </div>
              <div class="other-info">
                  <div class="socialmedia">
                      <h3 class="label-info">Redes Sociales</h3>
                      <i class="fab fa-twitter"></i>
                      <i class="fab fa-linkedin"></i>
                      <i class="fab fa-github"></i>
                      <i class="fab fa-meetup"></i>
                  </div>
                  <div class="socialmedia">
                      <h3 class="label-info">Repositorios</h3>
                      <div>
                          <a class="link-external" href="#">
                              <i class="fas fa-external-link-alt"></i>
                              https://github.com/amanzanod/hypotesis</a>
                      </div>
                  </div>
                  <div class="socialmedia">
                      <h3 class="label-info">Intereses</h3>
                      <div class="tags">
                          <span class="tag">Python</span>
                          <span class="tag">Django</span>
                          <span class="tag">Vue 2</span>
                          <span class="tag">Visual Studio Code</span>
                          <span class="tag">Postman</span>
                      </div>
                  </div>
              </div>

          </div>


          <div class="course-lists">
              <h3 class="label-info">Cursos</h3>

              <div class="hyp-card" v-for="course in courses" v-bind:key="course">
                  <div class="card-top">
                      <div class="card-img-course">
                          <div class="shadow-img"><i class="fas fa-sign-in-alt"></i></div>
                          <b-img class="card-course-img" :src="course.picture"></b-img>
                      </div>
                      <div class="card-info">
                          <h3 class="title">{{ course.name }}</h3>
                          <div class="other-info">
                              <div class="start_date">
                                  <i class="fas fa-calendar-alt"></i>
                                  <span>{{ course.start_at }}</span>
                              </div>
                              <div class="duration">
                                  <i class="far fa-clock"></i>
                                  <span>{{course.duration}} horas</span>
                              </div>
                          </div>
                      </div>
                  </div>
                  <div class="card-bottom">
                      <div class="card-progress">
                          <span class="value-progress">35%</span>
                          <div class="progress-total">
                              <div class="progress-current"></div>
                          </div>
                      </div>
                      <div v-if="course.teacher_main" class="teacher-course">
                          <div class="teacher">
                              <b-img class="card-teacher-img" :src="course.teacher_main.picture"></b-img>
                          </div>
                          <span class="teacher-name">{{ course.teacher_main.name }}</span>
                      </div>
                      <div class="course-users">
                          <i class="fas fa-users"></i>
                          <span class="users-value">{{ course.num_users }}</span>
                      </div>
                      <div class="action-course">
                          <div :class="user.state.alias">
                              Continuar
                          </div>
                      </div>
                  </div>

              </div>
          </div>

      </div>
  </div>

</template>

<script>

    import {HYP_MANAGER_USER, HYP_ENROL_ENROL, HYP_CONTEXT_COURSE} from '../api/constants';

    export default {
        name: 'UserProfile',
        components: {
        },
        data() {
            return {
                title: 'Perfil',
                create_href: '',
                contexts: 0,
                courses: [],
                user: {
                    name: null,
                    surname1: null,
                    username: null,
                    role: {
                        name: null
                    },
                    province: {
                        name: null
                    },
                    country: {
                        name: null
                    },
                    picture: null,
                    is_collapsed: false,
                    course: null,
                    about_me: '',
                    since: ''
                }
            }
        },
        beforeCreate () {
            this.username = localStorage.getItem("username");

            if (this.username === 'false') {
                this.$router.replace({ name: 'Login'});
            } else if (this.user === null) {
                this.$router.replace({ name: 'Login'});
            }

        },
        beforeMount () {
            this.axios
                .get( HYP_MANAGER_USER + this.username + '/?format=json')
                .then(response => {
                    let user = response.data;

                    if (user.username) {
                        this.user = user;
                        this.user.since = user.created_at.slice(0,4);
                    } else {
                        this.$router.replace({ name: 'Login'});
                    }
                });
            this.axios
                .get( HYP_ENROL_ENROL + this.username + '/contexts/?format=json')
                .then(response => {
                    let courses = response.data;

                    courses.forEach(element => {
                        this.axios
                            .get(HYP_CONTEXT_COURSE + element.context + '/?format=json')
                            .then(async response => {

                                let course = response.data;
                                course.num_users = 0;

                                if (course.teacher_main) {
                                    await this.axios
                                        .get(HYP_MANAGER_USER + course.teacher_main + '/?format=json')
                                        .then(response => {
                                            if (response.data.username) {
                                                course.teacher_main = response.data;
                                            }
                                        })
                                        .catch(error => {
                                            console.log(error)
                                        });
                                }

                                // Calculate Num Students.

                                await this.axios
                                    .get(HYP_ENROL_ENROL + course.alias + '/users/?format=json')
                                    .then(response => {
                                        if (response.data) {
                                            course.num_users = response.data.length;
                                        }
                                    })
                                    .catch(error => {
                                        console.log(error)
                                    });



                                this.courses.push(course);

                            })
                            .catch(error => {
                                console.log(error)
                            });

                    });
                })
        }
    }

</script>

<style scoped lang="scss">

    .container-header {
        background-color: #F6F6F6;
        border: 1px solid #DFDFDF;
        height: 153px;
        text-align: left;
        display: flex;
        align-items: center;
        padding: 0 50px;
        position: relative;
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
            right: -12px;
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

        .header-profile {
            display: flex;
            width: 100%;
            align-items: center;
            justify-content: space-between;
            position: relative;
            height: 244px;
            top: 86px;
            color: #B4B4B4;
            .data-left {
                position: relative;
                top: -10px;
                i.fas {
                    color: #636363;
                }
                .left-top {
                    font-size: 20px;
                    font-weight: 600;
                    margin-bottom: 7px;
                    >span {
                        margin-left: 11px;
                    }
                }
                .left-bottom {
                    font-size: 16px;
                    >span {
                        margin-left: 11px;
                    }
                }
            }
            .data-right {
                i.fas {
                    color: #636363;
                }
                top: -27px;
                position: relative;
                >span {
                    margin-right: 11px;
                }
            }
            .data-center {
                display: flex;
                flex-direction: column;
                align-items: center;
                position: relative;
                top: -13px;
                .picture_user {
                    width: 180px;
                    height: 180px;
                    overflow: hidden;
                    border-radius: 90px;
                    border: 8px solid #64a5af;
                    >img.picture_img {
                        height: 100%;
                    }
                }
                .user-name {
                    font-size: 28px;
                    font-weight: 600;
                    text-align: center;
                    color: #727475;
                }
                .user-title {
                    font-size: 20px;
                    font-weight: 600;
                    text-align: center;
                    color: #B4B4B4;
                }
            }

        }
    }

    #router-view {
        .container-view {
            background-color: white;
            border: 1px solid #DFDFDF;
            padding: 144px 30px 30px;
            display: flex;
            flex-direction: row;
            .info {
                text-align: left;
                width: 60%;
                .label-info {
                    font-size: 22px;
                    font-weight: 600;
                    color: #727475;
                }
                .aboutme {
                    font-size: 15px;
                    color: #A3A3A3;
                    font-family: "Varela Round", sans-serif;
                    line-height: 24px;
                    margin-bottom: 30px;
                    padding-right: 25px;
                }
                .other-info {
                    display: flex;
                    flex-direction: row;
                    flex-wrap: wrap;
                    .socialmedia {
                        width: 45%;
                        margin-bottom: 30px;
                        i.fab {
                            font-size: 28px;
                            margin-right: 22px;
                        }
                        i.fab.fa-twitter {
                            color: #257CD4;
                        }
                        i.fab.fa-linkedin {
                            color: #2D44A4;
                        }
                        i.fab.fa-github {
                            color: #000000;
                        }
                        i.fab.fa-meetup {
                            color: #D91544;
                        }
                        .tags {
                            .tag {
                                border: 1px solid #A3A3A3;
                                color: #A3A3A3;
                                font-size: 14px;
                                font-weight: 600;
                                padding: 4px 10px;
                                border-radius: 12px;
                                margin: 2px;
                                line-height: 14px;
                                white-space: nowrap;
                            }
                        }
                        .link-external {
                            color: #A3A3A3;
                        }
                    }
                }

            }
            .course-lists {
                width: 40%;
                text-align: left;

                .label-info {
                    font-size: 22px;
                    font-weight: 600;
                    color: #727475;
                }

                .hyp-card {
                    border: 1px solid #EEEEEE;
                    height: 167px;
                    margin-bottom: 15px;
                    .card-top {
                        display: flex;
                        flex-direction: row;
                        .card-img-course {
                            width: 200px;
                            min-width: 200px;
                            height: 120px;
                            overflow: hidden;
                            position: relative;
                            cursor: pointer;
                            .shadow-img {
                                background: rgba(100,165,175,1);
                                background: linear-gradient(to top, rgba(100,165,175,1) 0%, rgba(100,165,175,0) 100%);
                                position: absolute;
                                width: 200px;
                                height: 120px;
                                opacity: 0.8;
                                z-index: 5;
                                display: flex;
                                align-items: center;
                                justify-content: center;
                                &:hover {
                                    opacity: 1;
                                    i.fas.fa-sign-in-alt {
                                        font-size: 55px;
                                    }
                                }
                                i.fas.fa-sign-in-alt {
                                    position: absolute;
                                    font-size: 45px;
                                    color: white;
                                    transition: font-size 0.5s;
                                }
                            }
                            img.card-course-img {
                                width: 100%;
                            }
                        }
                        .card-info {
                            display: flex;
                            flex-direction: column;
                            width: 100%;
                            justify-content: space-between;
                            h3.title {
                                color: #727475;
                                font-size: 20px;
                                font-weight: 600;
                                margin: 10px;
                            }
                            .other-info {
                                display: flex;
                                justify-content: space-between;
                                color: #C7C7C7;
                                font-weight: 600;
                                font-size: 15px;
                                span {
                                    margin-left: 10px;
                                }
                                div {
                                    margin: 10px;
                                }
                            }
                        }
                    }
                    .card-bottom {
                        background-color: #F6F6F6;
                        height: 48px;
                        display: flex;
                        flex-direction: row;
                        justify-content: space-between;
                        .card-progress {
                            height: 100%;
                            display: flex;
                            align-items: center;
                            padding: 10px;
                            color: #A2A2A2;
                            font-size: 16px;
                            .progress-total {
                                width: 132px;
                                height: 23px;
                                border: 1px solid #A2A2A2;
                                border-radius: 14px;
                                margin-left: 10px;
                                display: flex;
                                align-items: center;

                                .progress-current {
                                    background-color: #2BC965;
                                    width: 59px;
                                    height: 11px;
                                    border-radius: 5px;
                                    margin-left: 8px;
                                }
                            }
                        }
                        .teacher-course {
                            display: flex;
                            flex-direction: row;
                            align-items: center;
                            .teacher {
                                width: 32px;
                                height: 32px;
                                border-radius: 16px;
                                overflow: hidden;
                                img.card-teacher-img {
                                    height: 100%;
                                }
                                .teacher {
                                    width: 10px;
                                    height: 10px;
                                    overflow: hidden;
                                }
                            }
                            span.teacher-name {
                                color: #A2A2A2;
                                font-size: 15px;
                                font-weight: 600;
                                margin-left: 10px;

                            }
                        }
                        .course-users {
                            display: flex;
                            align-items: center;
                            color: #A2A2A2;
                            font-size: 16px;
                            font-weight: 600;
                            i.fas.fa-users {
                                font-size: 27px;
                            }
                            span.users-value {
                                margin-left: 10px;
                            }
                        }
                        .action-course {
                            display: flex;
                            align-items: center;
                            padding: 20px;
                            .active {
                                background-color: #64A5AF;
                                color: white;
                                padding: 4px 10px;
                                border-radius: 10px;
                                font-size: 15px;
                                font-weight: 600;
                            }
                        }

                    }
                }


            }
        }
    }
</style>

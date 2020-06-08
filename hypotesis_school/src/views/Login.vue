<template>

    <div id="login">
        <b-modal ref="my-modal" hide-footer hide-header>
            <div class="d-block text-center">
                <h3>Usuario incorrecto</h3>
            </div>
        </b-modal>
        <div class="logo">
            <img id="logo_main" src="../assets/logo_login.svg"  alt="Hypotesis"/>
            <img id="logo_main_pro" src="../assets/pro.svg"  alt="PRO"/>
        </div>
        <div class="login-container">
            <div class="login-header">Inicia sesión en Hypotesis PRO</div>
            <div class="login-form">

                <b-form @submit="onSubmit" class="hyp-form" v-if="show">
                    <b-form-group id="input-group-1" label="USUARIO" label-for="input-1" class="hyp-login">
                        <i class="fas fa-at float-icon"></i>
                        <b-form-input
                                id="input-1"
                                v-model="form.username"
                                type="text"
                                required
                                placeholder="ingrese su usuario">
                        </b-form-input>
                    </b-form-group>
                    <b-form-group id="input-group-5" label="CONTRASEÑA" label-for="input-2" class="hyp-login">
                        <i class="fas fa-lock float-icon"></i>
                        <b-form-input
                                id="input-2"
                                v-model="form.password"
                                type="password"
                                required
                                placeholder="ingrese su contraseña"
                        ></b-form-input>
                    </b-form-group>

                    <b-button type="submit" variant="primary" class="hyp_submit">INICIAR SESIÓN</b-button>
                </b-form>
                <router-link class="recovery" :to="{ name: 'Login'}">¿Has olvidado la contraseña?</router-link>
            </div>
        </div>
        <span class="text-legal">Hypotesis PRO • Antonio Manzano Díaz • TFG Grado Multimedia</span>
    </div>


</template>

<script>

    import {
        HYP_MANAGER_USER
    } from '../api/constants';

    export default {
        name: 'Login',
        data() {
            return {
                show: true,
                form: {
                    username: '',
                    password: ''
                }
            }
        },
        methods: {
            onSubmit(evt) {
                evt.preventDefault();

                var formdata = new FormData();
                formdata.append("password", this.form.password);

                var requestOptions = {
                    method: 'POST',
                    body: formdata
                };

                fetch( HYP_MANAGER_USER + this.form.username + '/login/', requestOptions)
                    .then(response =>  {
                        if (response.status === 202) {
                            localStorage.setItem("username", this.form.username);
                            this.$router.replace({ name: 'Users'});
                        } else {
                            console.log(response);
                            this.showModal();
                        }
                    })
                    .catch(error => {
                        // Modal de error.
                        console.log('error', error);
                        }
                    );
            },
            showModal() {
                this.$refs['my-modal'].show()
            },
            hideModal() {
                this.$refs['my-modal'].hide()
            },
            toggleModal() {
                // We pass the ID of the button that we want to return focus to
                // when the modal has hidden
                this.$refs['my-modal'].toggle('#toggle-btn')
            }
        }
    }

</script>

<style  lang="scss">

    body {
        background-color: #66A6AF;
        #app {
            display: flex;
            align-items: center;
            justify-content: center;
            #login {
                .logo {
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                    align-items: center;
                    #logo_main {
                        width: 300px;
                    }
                    #logo_main_pro {
                        width: 91px;
                        margin: 10px 0 20px;
                    }
                }
                .login-container {
                    width: 556px;
                    background-color: #FFFFFF;
                    border: 1px solid #FFFFFF;
                    margin-bottom: 5px;
                    .login-header {
                        background-color: #E9E9E9;
                        height: 84px;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                        font-size: 22px;
                        color: #727475;
                    }
                    .login-form {
                        height: 330px;
                        padding: 18px;
                        display: flex;
                        flex-direction: column;
                        align-items: center;
                        .bv-no-focus-ring {
                            position: relative;
                            .float-icon {
                                position: absolute;
                                font-size: 24px;
                                color: #C2C2C2;
                                left: 7px;
                                top: 10px;
                            }
                        }
                        label {
                            font-size: 16px;
                            font-weight: 600;
                            color: #727475;
                        }
                        input {
                            width: 390px;
                            height: 45px;
                            text-align: center;
                            background-color: #F3F3F3;
                            border: 1px solid #C2C2C2;
                            font-size: 16px;
                            &::placeholder {
                                color: #b9b9b9;
                            }
                        }
                        button {
                            background-color: #1A5A64;
                            color: white;
                            width: 390px;
                            height: 39px;
                            margin: 20px 0;
                            font-size: 18px;
                            font-weight: 600;
                        }
                    }
                    .recovery {
                        font-weight: 600;
                        color: #727475;
                    }
                }
                .text-legal {
                    color: #373737;
                    font-size: 15px;
                    margin-top: 10px;
                }
            }

        }
    }



</style>

<template>

  <div id="router-view">
      <ContainerHeaderApp v-bind:subtitle="role" v-bind:title="title" v-bind:list="false"/>
      <div class="container-view">

          <b-form @submit="onSubmit" v-if="show" class="hyp-form">

              <b-form-group id="input-group-1" label="Nombre:" label-for="input-1" class="hyp-group">
                  <b-form-input
                          id="input-1"
                          v-model="form.name"
                          type="text"
                          required
                          placeholder="Nombre"></b-form-input>
              </b-form-group>

              <b-form-group id="input-group-2" label="Primer apellido:" label-for="input-2" class="hyp-group">
                  <b-form-input
                          id="input-2"
                          v-model="form.surname1"
                          type="text"
                          required
                          placeholder="Primer apellido"
                  ></b-form-input>
              </b-form-group>

              <b-form-group id="input-group-3" label="Segundo apellido:" label-for="input-3" class="hyp-group">
                  <b-form-input
                          id="input-3"
                          v-model="form.surname2"
                          type="text"
                          required
                          placeholder="Segundo apellido"
                  ></b-form-input>
              </b-form-group>

              <b-form-group id="input-group-4" label="Nombre de usuario:" label-for="input-4" class="hyp-group">
                  <b-form-input
                          id="input-4"
                          v-model="form.username"
                          type="text"
                          required
                          placeholder="Nombre de usuario"
                  ></b-form-input>
              </b-form-group>

              <b-form-group id="input-group-5" label="Contraseña:" label-for="input-5" class="hyp-group">
                  <b-form-input
                          id="input-5"
                          v-model="form.password"
                          type="password"
                          required
                          placeholder="Contraseña"
                  ></b-form-input>
              </b-form-group>

              <b-form-group id="input-group-6" label="Correo electrónico:" label-for="input-6" class="hyp-group">
                  <b-form-input
                          id="input-6"
                          v-model="form.email"
                          type="email"
                          required
                          placeholder="E-mail"
                  ></b-form-input>
              </b-form-group>

              <b-form-group id="input-group-7" label="Rol:" label-for="input-7" class="hyp-group">
                  <b-form-select
                          id="input-7"
                          v-model="form.role_id"
                          :options="roles"
                          required
                  ></b-form-select>
              </b-form-group>

              <b-form-group id="input-group-8" label="Dirección Postal:" label-for="input-8" class="hyp-group">
                  <b-form-input
                          id="input-8"
                          v-model="form.address"
                          type="text"
                          required
                          placeholder="Dirección postal completa"
                  ></b-form-input>
              </b-form-group>

              <b-form-group id="input-group-9" label="Código Postal:" label-for="input-9" class="hyp-group">
                  <b-form-input
                          id="input-9"
                          v-model="form.postal_code"
                          type="text"
                          required
                          placeholder="Código Postal"
                  ></b-form-input>
              </b-form-group>

              <b-form-group id="input-group-10" label="Ciudad:" label-for="input-10" class="hyp-group">
                  <b-form-input
                          id="input-10"
                          v-model="form.city"
                          type="text"
                          required
                          placeholder="Ciudad"
                  ></b-form-input>
              </b-form-group>

              <b-form-group id="input-group-11" label="Provincia:" label-for="input-11" class="hyp-group">
                  <b-form-select
                          id="input-11"
                          v-model="form.province_id"
                          :options="provinces"
                          required
                  ></b-form-select>
              </b-form-group>


              <b-form-group id="input-group-12" label="Acerca de mí:" label-for="input-12" class="hyp-group">
                  <b-form-textarea
                          id="input-12"
                          v-model="form.about_me"
                          placeholder="Escriba una descripción personal..."
                  ></b-form-textarea>
              </b-form-group>

              <b-form-group id="input-group-13" label="Imágen de perfil:" label-for="input-13" class="hyp-group">
                  <b-form-file
                          id="input-13"
                          accept="image/*"
                          v-model="form.picture"
                          :state="Boolean(form.picture)"
                          placeholder="Selecciona una imagen o arrastrala aquí..."
                          drop-placeholder="Arrastra aquí..."
                  ></b-form-file>
              </b-form-group>

              <b-form-group id="input-group-14" label="Idioma:" label-for="input-14" class="hyp-group">
                  <b-form-select
                          id="input-14"
                          v-model="form.language_id"
                          :options="languages"
                          required
                  ></b-form-select>
              </b-form-group>

              <div class="action_buttons">
                  <b-button type="submit" variant="primary" class="hyp_submit">Crear</b-button>
              </div>
          </b-form>

      </div>
  </div>

</template>

<script>

    import ContainerHeaderApp from '@/layouts/ContainerHeader.vue';
    import {
        HYP_MANAGER_USER,
        HYP_MANAGER_ROLE,
        HYP_MANAGER_PROVINCE,
        HYP_MANAGER_LANGUAGE,
        HYP_MANAGER_CREATE_USER
    } from '../api/constants';

    export default {
        name: 'User',
        components: {
            ContainerHeaderApp
        },
        data() {
            return {
                title: 'Usuario',
                role: '',
                roles: [],
                provinces: [],
                languages: [],
                form: {
                    name: '',
                    surname1: '',
                    surname2: '',
                    username: '',
                    password: '',
                    email: '',
                    role_id: null,
                    address: '',
                    postal_code: '',
                    city: '',
                    province_id: null,
                    country_id: 'ES',
                    state_id: 'active',
                    about_me: '',
                    picture: null,
                    language_id: null,
                },
                show: true
            }
        },
        beforeMount () {
            this.axios
                .get(HYP_MANAGER_USER + this.$route.params.username + '/?format=json')
                .then(response => {
                    const data = response.data;
                    this.title = data.name + ' ' + data.surname1 + ' ' + data.surname2;
                    this.role = data.role.name;
                    this.form.name = data.name;
                    this.form.surname1 = data.surname1;
                    this.form.surname2 = data.surname2;
                    this.form.username = data.username;
                    this.form.password = '*******';
                    this.form.email = data.email;
                    this.form.role_id = data.role.alias;
                    this.form.address = data.address;
                    this.form.postal_code = data.postal_code;
                    this.form.city = data.city;
                    this.form.province_id = data.province.code;
                    this.form.about_me = data.about_me;
                    this.form.picture = data.picture;
                    this.form.language_id = data.language.code;
                });
            this.axios
                .get( HYP_MANAGER_ROLE + '?format=json')
                .then(response => {
                    const data = response.data;
                    const options = [
                        { value: null, text: 'Selecciona el rol' }
                    ];

                    data.forEach(element => {
                        let option = {
                            value: element.alias,
                            text: element.name,
                            disabled: element.state !== 'active'
                        };
                        options.push(option);
                    });

                    this.roles = options;
                });
            this.axios
                .get( HYP_MANAGER_PROVINCE + '?format=json')
                .then(response => {
                    const data = response.data;
                    const options = [
                        { value: null, text: 'Selecciona la provincia' }
                    ];

                    data.forEach(element => {
                        let option = {
                            value: element.code,
                            text: element.name,
                        };
                        options.push(option);
                    });

                    this.provinces = options;
                });
            this.axios
                .get( HYP_MANAGER_LANGUAGE + '?format=json')
                .then(response => {
                    const data = response.data;
                    const options = [
                        { value: null, text: 'Seleccione el idioma' }
                    ];

                    data.forEach(element => {
                        let option = {
                            value: element.code,
                            text: element.name,
                        };
                        options.push(option);
                    });

                    this.languages = options;
                });
        },
        methods: {
            onSubmit(evt) {
                evt.preventDefault();
                this.axios
                    .post(HYP_MANAGER_CREATE_USER, this.form)
                    .then(response => {
                        alert(JSON.stringify(response));
                    })
                    .catch(error => {
                        alert(JSON.stringify(error));
                    });
            }
        }
    }

</script>

<style lang="scss">

    #router-view {
        .container-view {
            background-color: white;
            border: 1px solid #DFDFDF;
            padding: 30px;
            text-align: left;
            .hyp-form {
                display: flex;
                flex-direction: row;
                flex-wrap: wrap;
                .hyp-group {
                    width: 478px;
                    margin-right: 24px;
                    >label {
                        margin-bottom: 1px;
                        color: #727475;
                        font-weight: 600;
                    }
                    input, select, textarea, label.custom-file-label {
                        background-color: #EDEDED;
                        border: none;
                        font-size: 15px;
                        height: 45px;
                        color: black;
                        &::placeholder {
                            color: #b9b9b9;
                        }
                    }
                    textarea {
                        padding-top: 11px;
                    }
                    label.custom-file-label {
                        font-size: 15px;
                        color: #b9b9b9;
                        padding: 11px;
                    }
                }
                #input-group-8 {
                    width: 980px;
                }
                .action_buttons {
                    display: flex;
                    width: 100%;
                    justify-content: flex-end;
                    padding: 27px;
                    > button.hyp_submit {
                        background-color: #64a5af;
                        border: none;
                        &:hover {
                            background-color: #7dcad6;
                        }
                    }
                }
            }
        }

        .custom-file-input:lang(en) ~ .custom-file-label::after {
            content: 'Examinar';
            background-color: #64a5af;
            color: white;
            height: 45px;
            padding: 11px;
        }
    }
</style>

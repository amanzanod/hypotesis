<template>

    <div id="router-view">
        <ContainerHeaderApp v-bind:subtitle="subtitle" v-bind:title="title" v-bind:list="false"/>
        <div class="container-view">

            <b-modal ref="my-modal" hide-footer hide-header>
                <div class="d-block text-center">
                    <h3>{{ text_modal }}</h3>
                </div>
            </b-modal>

            <b-form @submit="onSubmit" v-if="show" class="hyp-form">

                <b-form-group id="input-group-1" label="Nombre:" label-for="input-1" class="hyp-group">
                    <b-form-input
                            id="input-1"
                            v-model="form.name"
                            type="text"
                            required
                            placeholder="Nombre"></b-form-input>
                </b-form-group>

                <b-form-group id="input-group-2" label="Alias:" label-for="input-2" class="hyp-group">
                    <b-form-input
                            id="input-2"
                            v-model="form.alias"
                            type="text"
                            required
                            placeholder="Nombre"></b-form-input>
                </b-form-group>

                <b-form-group id="input-group-3" label="Estado:" label-for="input-3" class="hyp-group">
                    <b-form-select
                            id="input-3"
                            v-model="form.state_id"
                            :options="states"
                            required
                    ></b-form-select>
                </b-form-group>

                <b-form-group id="input-group-4" label="Icono:" label-for="input-4" class="hyp-group">
                    <b-form-select
                            id="input-4"
                            v-model="form.icon"
                            :options="roles_icon"
                            required
                    ></b-form-select>
                </b-form-group>

                <b-form-group id="input-group-5" label="Descripción:" label-for="input-5" class="hyp-group">
                    <b-form-textarea
                            id="input-5"
                            v-model="form.description"
                            placeholder="Escriba una descripción ..."
                    ></b-form-textarea>
                </b-form-group>


                <b-form-group id="input-group-6" label-for="input-6" class="hyp-group">
                    <b-form-checkbox
                            id="input-6"
                            v-model="form.is_visible"
                            size="lg">Visible</b-form-checkbox>
                </b-form-group>



                <div class="action_buttons">
                    <router-link class="cancel" :to="{ name: 'Roles' }">Cancelar</router-link>
                    <b-button v-if="is_new" type="submit" variant="primary" class="hyp_submit">Crear</b-button>
                    <b-button v-else type="submit" variant="primary" class="hyp_submit">Editar</b-button>
                </div>
            </b-form>

        </div>
    </div>

</template>

<script>

    import ContainerHeaderApp from '@/layouts/ContainerHeader.vue';
    import {ROLE_ICONS} from '../api/options';
    import {
        HYP_MANAGER_ROLE,
        HYP_MANAGER_STATE,
    } from '../api/constants';

    export default {
        name: 'Role',
        components: {
            ContainerHeaderApp
        },
        data() {
            return {
                username: null,
                is_new: true,
                title: 'Rol',
                subtitle: '',
                text_modal: '',
                roles_icon: ROLE_ICONS,
                states: [],
                form: {
                    alias: '',
                    name: '',
                    state_id: null,
                    is_visible: '',
                    icon: null,
                    description: ''
                },
                show: true
            }
        },
        beforeMount () {
            this.alias = this.$route.params.alias;
            this.is_new = this.alias === '_new';

            this.alias = this.is_new ? null : this.alias;

            if (!this.is_new) {
                this.axios
                    .get(HYP_MANAGER_ROLE + this.alias + '/?format=json')
                    .then(response => {
                        const data = response.data;
                        this.title = data.name;
                        this.form.alias = data.alias;
                        this.form.name = data.name;
                        this.form.state_id = data.state.alias;
                        this.form.is_visible = data.is_visible;
                        this.form.icon = data.icon;
                        this.form.description = data.description;
                    });
            } else {
                this.title = 'Crear Rol';
            }

            this.axios
                .get( HYP_MANAGER_STATE + '?format=json')
                .then(response => {
                    const data = response.data;
                    const options = [
                        { value: null, text: 'Selecciona el estado' }
                    ];

                    data.forEach(element => {
                        let option = {
                            value: element.alias,
                            text: element.name
                        };
                        options.push(option);
                    });

                    this.states = options;
                });

        },
        methods: {
            onSubmit(evt) {
                evt.preventDefault();
                if (this.is_new) {
                    this.axios
                        .post(HYP_MANAGER_ROLE, this.form)
                        .then(response => {
                            console.log(response);
                            this.text_modal = 'Se ha creado el rol';
                            this.$router.replace({ name: 'Roles'});

                        })
                        .catch(error => {
                            console.log(error);
                            this.text_modal = 'No se ha podido crear el rol';
                            this.showModal();
                        });
                } else {
                    var myHeaders = new Headers();
                    myHeaders.append("Content-Type", "application/json");

                    var raw = JSON.stringify(
                        this.form
                        );

                    var requestOptions = {
                        method: 'PUT',
                        headers: myHeaders,
                        body: raw,
                        redirect: 'follow'
                    };

                    fetch(HYP_MANAGER_ROLE + this.alias + '/', requestOptions)
                        .then(response => {
                            console.log(response);
                            this.text_modal = 'Los cambios se han guardado';
                            this.$router.replace({ name: 'Roles'});
                        })
                        .then(result => console.log(result))
                        .catch(error => {
                            console.log(error);
                            this.text_modal = 'Hubo un error en la petición';
                            this.showModal();
                        });
                }

            },
            showModal() {
                this.$refs['my-modal'].show()
            },
            hideModal() {
                this.$refs['my-modal'].hide();
            },
            toggleModal() {
                // We pass the ID of the button that we want to return focus to
                // when the modal has hidden
                this.$refs['my-modal'].toggle('#toggle-btn');
                this.$refs['my-modal'].hide();
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
                    .custom-control.custom-checkbox {
                        margin-top: 32px;
                    }
                    textarea {
                        padding-top: 11px;
                    }
                    label.custom-file-label {
                        font-size: 15px;
                        color: #b9b9b9;
                        padding: 11px;
                    }
                    &.image {
                        .bv-no-focus-ring {
                            display: flex;
                            flex-direction: row;
                            div.image_browser {
                                width: 420px;
                            }
                            .no_image {
                                width: 45px;
                                height: 45px;
                                background-color: #ededed;
                                margin-left: 13px;
                                border-radius: 5px;
                                display: flex;
                                align-items: center;
                                justify-content: center;
                                i.fas.fa-camera-retro {
                                    font-size: 27px;
                                    color: #cccccc;
                                }
                            }
                            img.preview.img-fluid.rounded.d-block {
                                width: 45px;
                                height: 45px;
                                border-radius: 5px;
                                margin-left: 10px;
                            }
                        }

                    }

                }
                .action_buttons {
                    display: flex;
                    width: 100%;
                    justify-content: flex-end;
                    padding: 27px;
                    > button.hyp_submit {
                        background-color: #64a5af;
                        border: none;
                        z-index: 2;
                        &:hover {
                            background-color: #7dcad6;
                        }
                    }
                    a.cancel {
                        color: grey;
                        background-color: #e8e8e8;
                        padding: 6px 12px;
                        font-size: 15px;
                        border-radius: 7px;
                        position: relative;
                        left: 7px;
                        z-index: 2;
                        &:hover {
                            text-decoration: none;
                            background-color: #d1d1d1;
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

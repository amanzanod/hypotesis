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


                <b-form-group id="input-group-1" label="Rol:" label-for="input-1" class="hyp-group">
                    <b-form-select
                            id="input-1"
                            v-model="form.role_id"
                            :options="roles"
                            required
                    ></b-form-select>
                </b-form-group>

                <b-form-group id="input-group-2" label="Permiso:" label-for="input-2" class="hyp-group">
                    <b-form-select
                            id="input-2"
                            v-model="form.permission_id"
                            :options="permissions"
                            required
                    ></b-form-select>
                </b-form-group>


                <b-form-group id="input-group-3" label-for="input-3" class="hyp-group">
                    <b-form-checkbox
                            id="input-3"
                            v-model="form.is_active"
                            size="lg">Activo</b-form-checkbox>
                </b-form-group>



                <div class="action_buttons">
                    <router-link class="cancel" :to="{ name: 'Roles' }">Cancelar</router-link>
                    <b-button type="submit" variant="primary" class="hyp_submit">Asignar</b-button>
                </div>
            </b-form>

        </div>
    </div>

</template>

<script>

    import ContainerHeaderApp from '@/layouts/ContainerHeader.vue';

    import {
        HYP_MANAGER_PERMISSION,
        HYP_MANAGER_ROLE,
        HYP_MANAGER_ROLEPERMISSION
    } from '../api/constants';

    export default {
        name: 'AssignPermissions',
        components: {
            ContainerHeaderApp
        },
        data() {
            return {
                username: null,
                image: null,
                imageSrc: null,
                is_new: true,
                title: 'Asignar permisos',
                subtitle: '',
                text_modal: '',
                roles: [],
                permissions: [],
                form: {
                    role_id: null,
                    permission_id: null,
                    is_active: true,
                },
                show: true
            }
        },
        beforeMount () {

            this.axios
                .get( HYP_MANAGER_ROLE+ '?format=json')
                .then(response => {
                    const data = response.data;
                    const options = [
                        { value: null, text: 'Selecciona el rol' }
                    ];

                    data.forEach(element => {
                        let option = {
                            value: element.alias,
                            text: element.name
                        };
                        options.push(option);
                    });

                    this.roles = options;
                });


            this.axios
                .get( HYP_MANAGER_PERMISSION + '?format=json')
                .then(response => {
                    const data = response.data;
                    const options = [
                        { value: null, text: 'Selecciona el permiso' }
                    ];

                    data.forEach(element => {
                        let option = {
                            value: element.alias,
                            text: element.alias
                        };
                        options.push(option);
                    });

                    this.permissions = options;
                });

        },
        methods: {
            onSubmit(evt) {
                evt.preventDefault();
                this.axios
                    .post(HYP_MANAGER_ROLEPERMISSION, this.form)
                    .then(response => {
                        console.log(response);
                        this.text_modal = 'Se ha asignado el permiso';
                        this.$router.replace({ name: 'Roles'});

                    })
                    .catch(error => {
                        console.log(error);
                        this.text_modal = 'No se ha podido asignar el permiso';
                        this.showModal();
                    });

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
                    width: 420px;
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

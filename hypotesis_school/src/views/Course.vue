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

                <b-form-group id="input-group-4" label="Formato:" label-for="input-4" class="hyp-group">
                    <b-form-select
                            id="input-4"
                            v-model="form.format_id"
                            :options="formats"
                            required
                    ></b-form-select>
                </b-form-group>

                <b-form-group id="input-group-6" label="Idioma:" label-for="input-6" class="hyp-group">
                    <b-form-select
                            id="input-6"
                            v-model="form.language_id"
                            :options="languages"
                            required
                    ></b-form-select>
                </b-form-group>

                <b-form-group id="input-group-7" label="Nivel:" label-for="input-7" class="hyp-group">
                    <b-form-select
                            id="input-7"
                            v-model="form.level_id"
                            :options="levels"
                            required
                    ></b-form-select>
                </b-form-group>

                <b-form-group id="input-group-8" label="Categoría:" label-for="input-8" class="hyp-group">
                    <b-form-select
                            id="input-8"
                            v-model="form.category_id"
                            :options="categories"
                            required
                    ></b-form-select>
                </b-form-group>

                <b-form-group id="input-group-14" label="Profesor Principal:" label-for="input-14" class="hyp-group">
                    <b-form-select
                            id="input-14"
                            v-model="form.teacher_main"
                            :options="teachers"
                            required
                    ></b-form-select>
                </b-form-group>

                <b-form-group id="input-group-12" label="Duración (horas):" label-for="input-12" class="hyp-group">
                    <b-form-input
                            id="input-12"
                            v-model="form.duration"
                            type="number"
                            required
                            placeholder="Duración en horas"></b-form-input>
                </b-form-group>

                <b-form-group id="input-group-13" label="Etiquetas:" label-for="input-13" class="hyp-group">
                    <b-form-input
                            id="input-13"
                            v-model="form.tech_tags"
                            type="text"
                            placeholder="Etiquetas separadas por coma"></b-form-input>
                </b-form-group>

                <b-form-group id="input-group-9" label="Descripción:" label-for="input-9" class="hyp-group">
                    <b-form-textarea
                            id="input-9"
                            v-model="form.description"
                            placeholder="Escriba una descripción ..."
                    ></b-form-textarea>
                </b-form-group>

                <b-form-group id="input-group-10" label="Syllabus:" label-for="input-10" class="hyp-group">
                    <b-form-textarea
                            id="input-10"
                            v-model="form.syllabus"
                            placeholder="Escriba el syllabus ..."
                    ></b-form-textarea>
                </b-form-group>

                <b-form-group id="input-group-11" label="Requisitos:" label-for="input-11" class="hyp-group">
                    <b-form-textarea
                            id="input-11"
                            v-model="form.requeriments"
                            placeholder="Escriba los requisitos ..."
                    ></b-form-textarea>
                </b-form-group>

                <b-form-group id="input-group-15" label="Imágen:" label-for="input-15" class="hyp-group image">
                    <b-form-file
                            class="image_browser"
                            id="input-15"
                            accept="image/*"
                            v-model="image"
                            :state="Boolean(form.picture)"
                            placeholder="Selecciona una imagen o arrastrala aquí..."
                            drop-placeholder="Arrastra aquí..."
                    ></b-form-file>
                    <b-img v-if="imageSrc" :src="imageSrc" class="preview" fluid block rounded></b-img>
                    <div class="no_image" v-else><i class="fas fa-camera-retro"></i></div>
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

    import {
        HYP_CONTEXT_COURSE,
        HYP_CONTEXT_FORMAT,
        HYP_CONTEXT_STATE,
        HYP_CONTEXT_LEVEL,
        HYP_CONTEXT_LANGUAGE,
        HYP_CONTEXT_CATEGORY,
        HYP_MANAGER_ROLE
    } from '../api/constants';

    const base64Encode = data =>
        new Promise((resolve, reject) => {
            const reader = new FileReader();
            reader.readAsDataURL(data);
            reader.onload = () => resolve(reader.result);
            reader.onerror = error => reject(error);
        });

    export default {
        name: 'Course',
        components: {
            ContainerHeaderApp
        },
        data() {
            return {
                username: null,
                is_new: true,
                title: 'Curso',
                image: null,
                imageSrc: null,
                subtitle: '',
                text_modal: '',
                states: [],
                formats: [],
                levels: [],
                categories: [],
                languages: [],
                teachers: [],
                form: {
                    type_id: 'course',
                    parent_id: 'hyppro',
                    alias: '',
                    name: '',
                    state_id: null,
                    format_id: null,
                    level_id: null,
                    language_id: null,
                    category_id: null,
                    duration: null,
                    teacher_main: null,
                    tech_tags: '',
                    syllabus: '',
                    description: '',
                    requeriments: '',
                    picture: null
                },
                show: true
            }
        },
        computed: {
            hasImage() {
                return !!this.image;
            }
        },
        watch: {
            image(newValue, oldValue) {
                if (newValue !== oldValue) {
                    if (newValue) {
                        base64Encode(newValue)
                            .then(value => {
                                this.imageSrc = value;
                            })
                            .catch(() => {
                                this.imageSrc = null;
                            });
                    } else {
                        this.imageSrc = null;
                    }
                }
            }
        },
        beforeMount () {
            this.alias = this.$route.params.alias;
            this.is_new = this.alias === '_new';

            this.alias = this.is_new ? null : this.alias;

            if (!this.is_new) {
                this.axios
                    .get(HYP_CONTEXT_COURSE + this.alias + '/?format=json')
                    .then(response => {
                        const data = response.data;
                        this.title = data.name;
                        this.form.alias = data.alias;
                        this.form.name = data.name;
                        this.form.state_id = data.state.alias;
                        this.form.format_id = data.format ? data.format.alias : null;
                        this.form.syllabus = data.syllabus;
                        this.form.requeriments = data.requeriments;
                        this.form.language_id = data.language.code;
                        this.form.level_id = data.level ? data.level.alias : null;
                        this.form.category_id = data.category.alias;
                        this.form.description = data.description;
                        this.form.duration = data.duration;
                        this.form.tech_tags = data.tech_tags;
                        this.form.teacher_main = data.teacher_main;
                        this.form.picture = data.picture;
                    });
            } else {
                this.title = 'Crear Curso';
            }

            this.axios
                .get( HYP_CONTEXT_STATE + '?format=json')
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

            this.axios
                .get( HYP_CONTEXT_FORMAT + '?format=json')
                .then(response => {
                    const data = response.data;
                    const options = [
                        { value: null, text: 'Selecciona el formato' }
                    ];

                    data.forEach(element => {
                        let option = {
                            value: element.alias,
                            text: element.name
                        };
                        options.push(option);
                    });

                    this.formats = options;
                });

            this.axios
                .get( HYP_CONTEXT_LANGUAGE + '?format=json')
                .then(response => {
                    const data = response.data;
                    const options = [
                        { value: null, text: 'Selecciona el idioma' }
                    ];

                    data.forEach(element => {
                        let option = {
                            value: element.code,
                            text: element.name
                        };
                        options.push(option);
                    });

                    this.languages = options;
                });

            this.axios
                .get( HYP_CONTEXT_LEVEL + '?format=json')
                .then(response => {
                    const data = response.data;
                    const options = [
                        { value: null, text: 'Selecciona el nivel' }
                    ];

                    data.forEach(element => {
                        let option = {
                            value: element.alias,
                            text: element.name
                        };
                        options.push(option);
                    });

                    this.levels = options;
                });

            this.axios
                .get( HYP_CONTEXT_CATEGORY + 'course/filter/?format=json')
                .then(response => {
                    const data = response.data;
                    const options = [
                        { value: null, text: 'Selecciona la categoría' }
                    ];

                    data.forEach(element => {
                        let option = {
                            value: element.alias,
                            text: element.name
                        };
                        options.push(option);
                    });

                    this.categories = options;
                });

            this.axios
                .get( HYP_MANAGER_ROLE + 'teacherpro/users/?format=json')
                .then(response => {
                    const data = response.data;
                    const options = [
                        { value: null, text: 'Selecciona el profesor principal' }
                    ];

                    data.forEach(element => {
                        let option = {
                            value: element.username,
                            text: element.name + ' ' + element.surname1 + ' ' + element.surname2
                        };
                        options.push(option);
                    });

                    this.teachers = options;
                });

        },
        methods: {
            onSubmit(evt) {
                evt.preventDefault();
                if (this.is_new) {

                    this.form.picture = this.image;

                    let myHeaders = new Headers();
                    myHeaders.append("Content-Type", "application/json");

                    let raw = JSON.stringify(
                        this.form
                    );

                    let requestOptions = {
                        method: 'POST',
                        headers: myHeaders,
                        body: raw,
                        redirect: 'follow'
                    };

                    fetch(HYP_CONTEXT_COURSE, requestOptions)
                        .then(response => {
                            console.log(response);
                            if (response.status < 300) {
                                this.text_modal = 'Se ha creado el curso';
                                this.$router.replace({ name: 'Courses'});
                            } else {
                                this.text_modal = 'No se ha podido crear el curso';
                                this.showModal();
                            }
                        })
                        .then(result => console.log(result))
                        .catch(error => {
                            console.log(error);
                            this.text_modal = 'Hubo un error en la creación del curso';
                            this.showModal();
                        });




                } else {
                    let myHeaders = new Headers();
                    myHeaders.append("Content-Type", "application/json");

                    let raw = JSON.stringify(
                        this.form
                        );

                    let requestOptions = {
                        method: 'PUT',
                        headers: myHeaders,
                        body: raw,
                        redirect: 'follow'
                    };

                    fetch(HYP_CONTEXT_COURSE + this.alias + '/', requestOptions)
                        .then(response => {
                            console.log(response);
                            if (response.status < 300) {
                                this.text_modal = 'Se ha actualizado el curso';
                                this.$router.replace({ name: 'Courses'});
                            } else {
                                this.text_modal = 'No se ha podido actualizar el curso';
                                this.showModal();
                            }
                        })
                        .then(result => console.log(result))
                        .catch(error => {
                            console.log(error);
                            this.text_modal = 'Hubo un error en la petición';
                            this.showModal();
                        });
                }

            },
            getImage(event){
                //Asignamos la imagen a  nuestra data
                this.imagen = event.target.files[0];
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

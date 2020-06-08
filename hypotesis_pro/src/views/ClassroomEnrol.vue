<template>

  <div id="router-view">
      <ContainerHeaderApp v-bind:subtitle="subtitle" v-bind:title="title" v-bind:list="false"/>
      <div class="container-view">

          <b-modal ref="my-modal" hide-footer hide-header>
              <div class="d-block text-center">
                  <h3>{{ text_modal }}</h3>
              </div>
          </b-modal>

          <div class="users_total">
              <h3 class="enrol_title">Usuarios</h3>
              <div class="action_table">
                  <div class="search_table">
                      <b-form-input
                              v-model="filter"
                              type="search"
                              id="filterInput"
                              placeholder="Buscar"
                      ></b-form-input>
                      <span class="search_input"><i class="fas fa-search"></i></span>
                  </div>
              </div>
              <b-form-group>
                  <b-form-checkbox-group id="checkbox-group-1" v-model="users_selected_assign" name="flavour-1">
                      <b-table striped
                               hover
                               :items="items"
                               :fields="fields"
                               sort-icon-left
                               :filter="filter"
                               @filtered="onFiltered"
                               responsive="sm"
                               :tbody-tr-class="rowClass">
                          <template v-slot:cell(state)="state">
                              <span v-html="state.value"></span>
                          </template>
                          <template v-slot:cell(name)="data">
                              <div class="user-name">
                                  <div class="picture_mini">
                                      <b-img :src="data.item.picture"></b-img>
                                  </div>
                                  <div class="data">
                                      <a class="fullname">{{ data.value }}</a>
                                      <span class="title">{{ data.item.title }}</span>
                                  </div>
                              </div>
                          </template>
                          <template v-slot:cell(select)="data">
                              <b-form-checkbox :value="data.item.username" size="lg"></b-form-checkbox>
                          </template>
                      </b-table>
                  </b-form-checkbox-group>
              </b-form-group>
          </div>

          <div class="assign_buttons">
              <div class="assign_btn" v-on:click="assign_users"><i class="fas fa-chevron-right"></i></div>
              <div class="unassign_btn" v-on:click="unassign_users"><i class="fas fa-chevron-left"></i></div>
          </div>

          <div class="users_selected">
              <h3 class="enrol_title">Estudiantes Matriculados</h3>
              <div class="action_table">
                  <div class="search_table">
                      <b-form-input
                              v-model="filter2"
                              type="search"
                              id="filterInput2"
                              placeholder="Buscar"
                      ></b-form-input>
                      <span class="search_input"><i class="fas fa-search"></i></span>
                  </div>
              </div>
              <b-form-group>
                  <b-form-checkbox-group id="checkbox-group-2" v-model="users_selected_unassign" name="flavour-2">
                      <b-table striped
                               hover
                               :items="items2"
                               :fields="fields2"
                               sort-icon-left
                               :filter="filter2"
                               @filtered="onFiltered"
                               responsive="sm"
                               :tbody-tr-class="rowClass">
                          <template v-slot:cell(state)="state">
                              <span v-html="state.value"></span>
                          </template>
                          <template v-slot:cell(id)="data">
                              <span>{{data.item.id}}</span>
                          </template>
                          <template v-slot:cell(name)="data">
                              <div class="user-name">
                                  <div class="picture_mini">
                                      <b-img :src="data.item.picture"></b-img>
                                  </div>
                                  <div class="data">
                                      <a class="fullname">{{ data.value }}</a>
                                      <span class="title">{{ data.item.title }}</span>
                                  </div>
                              </div>
                          </template>
                          <template v-slot:cell(select)="data">
                              <b-form-checkbox :value="data.item.id" size="lg"></b-form-checkbox>
                          </template>
                      </b-table>
                  </b-form-checkbox-group>
              </b-form-group>
          </div>



      </div>
  </div>

</template>

<script>

    import ContainerHeaderApp from '@/layouts/ContainerHeader.vue';
    import {HYP_MANAGER_USER, HYP_ENROL_ENROL} from '../api/constants';

    export default {
        name: 'ClassroomEnrol',
        components: {
            ContainerHeaderApp
        },
        data() {
            return {
                title: 'Matriculación Aula',
                users: '0',
                selected: null,
                filter: null,
                filter2: null,
                text_modal: '',
                users_selected: [],
                users_selected_assign: [],
                users_selected_unassign: [],
                users_selectables: [],
                fields: [
                    {
                        key: 'state',
                        label: 'Estado',
                        class: ['text-center', 'vertical-align'],
                        sortable: true,
                        formatter: (value) => {
                            switch (value.alias) {
                                case 'active':
                                    return `<i class="fas fa-check-circle"></i>`;
                                case 'unactive':
                                    return `<i class="fas fa-minus-circle"></i>`;
                            }
                        }
                    },
                    {
                        key: 'name',
                        label: 'Nombre',
                        class: 'text-left',
                        sortable: true,
                        formatter: (value, key, item) => {
                            return item.name + ' ' + item.surname1 + ' ' + item.surname2
                        }
                    },
                    {
                        key: 'username',
                        label: 'Usuario',
                        class: 'text-left',
                        sortable: true
                    },
                    {
                        key: 'role',
                        label: 'Rol',
                        class: 'text-left',
                        sortable: true,
                        formatter: (value) => {
                            return value.name
                        }
                    },
                    {
                        key: 'select',
                        label: 'Seleccionar'
                    }
                ],
                fields2: [
                    {
                        key: 'select',
                        label: 'Seleccionar'
                    },
                    {
                        key: 'id',
                        label: 'Id',
                        formatter: (value, key, item) => {
                            return item.id
                        }
                    },
                    {
                        key: 'name',
                        label: 'Nombre',
                        class: 'text-left',
                        sortable: true,
                        formatter: (value, key, item) => {
                            return item.name + ' ' + item.surname1 + ' ' + item.surname2
                        }
                    },
                    {
                        key: 'username',
                        label: 'Usuario',
                        class: 'text-left',
                        sortable: true
                    },
                    {
                        key: 'role',
                        label: 'Rol',
                        class: 'text-left',
                        sortable: true,
                        formatter: (value) => {
                            return value.alias
                        }
                    },
            ],
                items: null,
                items2: [],
            }
        },
        async beforeMount() {
            this.alias = this.$route.params.alias;
            this.subtitle = this.alias;
            await this.axios
                .get(HYP_MANAGER_USER + '?format=json')
                .then(response => {
                    this.items = response.data;
                    this.users = response.data.length + '';
                    this.users_selectables = this.users;
                });
            await this.axios
                .get(HYP_ENROL_ENROL + this.alias + '/students/?format=json')
                .then(response => {
                    let users_enrol = response.data;
                    users_enrol.forEach(element => {
                        this.axios
                            .get(HYP_MANAGER_USER + element.user + '/?format=json')
                            .then(response => {
                                response.data.id = element.id;
                                this.items2.push(response.data);
                            });
                        let username = element.user;
                        if (username) {
                            this.items = this.items.filter(function (el) {
                                return el.username !== username;
                            });
                        }


                    });
                });
        },
        methods: {
            rowClass(item, type) {
                if (!item || type !== 'row') return;
                if (item.is_visible === false) return 'text-muted';
            },
            onFiltered(filteredItems) {
                // Trigger pagination to update the number of buttons/pages due to filtering
                this.users = filteredItems.length;
            },
            assign_users() {
                this.users_selected_assign.forEach(element => {

                    var formdata = new FormData();
                    formdata.append("user", element);
                    formdata.append("context", this.alias );
                    formdata.append("role", "student");
                    formdata.append("state_id", "active");

                    var requestOptions = {
                        method: 'POST',
                        body: formdata,
                        redirect: 'follow'
                    };

                    fetch(HYP_ENROL_ENROL, requestOptions)
                        .then(response => {
                            console.log(response);
                            if (response.status < 300) {
                                location.reload();
                            } else {
                                this.text_modal = 'No se han podido matricular.';
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
                );

            },
            unassign_users() {

                this.users_selected_unassign.forEach(element => {

                        var requestOptions = {
                            method: 'DELETE',
                            redirect: 'follow'
                        };

                        fetch( HYP_ENROL_ENROL + element + '/', requestOptions)
                            .then(response => {
                                console.log(response);
                                if (response.status < 300) {
                                    location.reload();
                                } else {
                                    this.text_modal = 'No se han podido desmatricular.';
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
                );
            }
        }
    }

</script>

<style scoped lang="scss">

    #router-view {
        h3.enrol_title{
            font-family: "Montserrat", sans-serif;
            font-size: 22px;
            font-weight: 600;
            margin-bottom: 5px;
            color: #8e8e8e;
            text-align: left;
        }
        .container-view {
            background-color: white;
            border: 1px solid #DFDFDF;
            padding: 30px;
            display: flex;
            flex-direction: row;
            .users_total {
                width: 700px;
                margin-right: 20px;
            }
            .users_selected {
                width: 700px;
            }
            .assign_buttons {
                width: 55px;
                display: flex;
                flex-direction: column;
                justify-content: center;
                color: white;
                .assign_btn {
                    height: 40px;
                    width: 40px;
                    background-color: #64a5af;
                    border-radius: 20px;
                    margin-bottom: 20px;
                    cursor: pointer;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                }
                .unassign_btn {
                    height: 40px;
                    width: 40px;
                    background-color: #7f7f7f;
                    border-radius: 20px;
                    cursor: pointer;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                }
            }
            .action_table {
                display: flex;
                .search_table {
                    position: relative;
                    width: 100%;
                    margin-right: 0;
                    input#filterInput {
                        width: 100%;
                        height: 45px;
                        border-radius: 0;
                        margin-bottom: 10px;
                        position: relative;
                        border: 1px solid #DFDFDF;
                    }
                    input#filterInput2 {
                        width: 100%;
                        height: 45px;
                        border-radius: 0;
                        margin-bottom: 10px;
                        position: relative;
                        border: 1px solid #DFDFDF;
                    }
                    .search_input {
                        display: block;
                        position: absolute;
                        top: 8px;
                        right: 19px;
                        font-size: 20px;
                        color: #64a5af;
                    }
                }
                .custom-select {
                    width: 250px;
                    margin-right: 10px;
                    height: 45px;
                    border-radius: 0;
                    border: 1px solid #DFDFDF;
                }
                .filter_options {
                    width: 45px;
                    min-width: 45px;
                    height: 45px;
                    background-color: #64a5af;
                    color: white;
                    font-size: 22px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                }
            }

        }
    }

    .table.b-table {
        font-size: 14px;
        thead {
            border: 1px solid #DFDFDF;
            background-color: #F6F6F6;
        }
        tbody {
            tr {
                td {
                    vertical-align: middle;
                    padding: 6px;
                }
                border: 1px solid #DFDFDF;
                &:nth-of-type(odd) {
                    background-color: rgba(0, 0, 0, 0.02);
                }
                a{
                    color: #64A5AF;
                    font-weight: 600;
                    &.relation {
                        border: 1px solid #64A5AF;
                        border-radius: 10px;
                        padding: 4px 10px;
                        &:hover {
                            text-decoration: none;
                            background-color: #64A5AF;
                            color: white !important;
                        }
                    }
                }

                .user-name {
                    display: flex;
                    flex-direction: row;
                    .picture_mini {
                        width: 36px;
                        height: 36px;
                        margin-right: 7px;
                        border-radius: 18px;
                        overflow: hidden;
                        >img {
                            width: 36px;
                        }
                    }
                    .data {
                        display: flex;
                        flex-direction: column;
                        .fullname {

                        }
                        span.title {
                            font-size: 13px;
                            line-height: 8px;
                            color: #638f96;
                        }
                    }
                }

                i.fas {
                    font-size: 20px;
                    &.fa-check-circle {
                        color: #28BB72;
                    }
                    &.fa-minus-circle {
                        color: #E9782D;
                    }
                    &.fa-eye {
                        color: #0190D8;
                        margin-right: 8px;
                    }
                    &.fa-eye-slash {
                        color: rgba(69, 69, 69, 0.18);
                        margin-right: 8px;
                    }
                    &.fa-trash-alt {
                        color: #FF0000;
                        margin-right: 8px;
                    }
                    &.fa-cog {
                        color: #E99322;
                    }
                }
                &.text-muted {
                    opacity: 0.5;
                }

            }
        }
    }



</style>

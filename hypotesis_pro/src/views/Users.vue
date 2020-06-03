<template>

  <div id="router-view">
      <ContainerHeaderApp v-bind:subtitle="users" v-bind:title="title" v-bind:list="true" v-bind:create_href="create_href"/>
      <div class="container-view">

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
              <b-form-select v-model="filter" :options="options"></b-form-select>
              <span class="filter_options"><i class="fas fa-filter"></i></span>
          </div>


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
              <template v-slot:cell(role)="data">
                  <router-link class="relation" :to="{ name: 'Role', params: { alias: data.item.role.alias }}">{{ data.item.role.name }}</router-link>
              </template>
              <template v-slot:cell(actions)="actions">
                  <span v-html="actions.value"></span>
              </template>
              <template v-slot:cell(name)="data">
                  <div class="user-name">
                      <div class="picture_mini">
                        <b-img :src="data.item.picture"></b-img>
                      </div>
                      <div class="data">
                          <router-link class="fullname" :to="{ name: 'User', params: { username: data.item.username }}">{{ data.value }}</router-link>
                          <span class="title">{{ data.item.title }}</span>
                      </div>
                  </div>
              </template>
          </b-table>



      </div>
  </div>

</template>

<script>

    import ContainerHeaderApp from '@/layouts/ContainerHeader.vue';
    import {HYP_MANAGER_USER, HYP_MANAGER_ROLE} from '../api/constants';

    export default {
        name: 'Users',
        components: {
            ContainerHeaderApp
        },
        data() {
            return {
                title: 'Usuarios Registrados',
                users: '0',
                create_href: '/users/_new',
                selected: null,
                options: [],
                filter: null,
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
                        key: 'role',
                        label: 'Rol',
                        class: 'text-left',
                        sortable: true
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
                        key: 'email',
                        label: 'E-mail',
                        class: 'text-left',
                    },
                    {
                        key: 'username',
                        label: 'Usuario',
                        class: 'text-left',
                        sortable: true
                    },
                    {
                        key: 'country',
                        label: 'País',
                        class: 'text-left',
                        sortable: true,
                        formatter: (value) => {
                            return value.name
                        }
                    },
                    {
                        key: 'updated_at',
                        label: 'Último Acceso',
                        class: 'text-left',
                        sortable: true,
                        formatter: (value) => {
                            return value
                        }

                    },
                    {
                        key: 'actions',
                        label: 'Acciones',
                        formatter: (value, key, item) => {
                            let html = ``;
                            if (item.is_visible === true) {
                                html += `<b-button v-b-tooltip.hover href="/${item.username}" title="Visible">
                                            <i class="fas fa-eye"></i>
                                         </b-button>`;
                            } else {
                                html += `<b-button v-b-tooltip.hover href="/${item.username}" title="No Visible">
                                            <i class="fas fa-eye-slash"></i>
                                         </b-button>`;
                            }

                            html += `<a href="/${item.username}"><i class="fas fa-trash-alt"></i></a>`;
                            html += `<a href="/${item.username}"><i class="fas fa-cog"></i></a>`;
                            return html;
                        }
                    }
                ],
                items: null
            }
        },
        beforeMount () {
            this.axios
                .get( HYP_MANAGER_USER + '?format=json')
                .then(response => {
                    this.items = response.data;
                    this.users = response.data.length + '';
                });
            this.axios
                .get( HYP_MANAGER_ROLE + '?format=json')
                .then(response => {
                    const data = response.data;
                    const options = [
                        { value: null, text: 'Todos los roles' }
                        ];

                    data.forEach(element => {
                        let option = {
                            value: element.alias,
                            text: element.name,
                            disabled: element.state.alias !== 'active'
                        };
                        options.push(option);
                    });

                    this.options = options;
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
            .action_table {
                display: flex;
                .search_table {
                    position: relative;
                    width: 100%;
                    margin-right: 10px;
                    input#filterInput {
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

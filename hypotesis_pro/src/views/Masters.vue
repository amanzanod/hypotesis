<template>

  <div id="router-view">
      <ContainerHeaderApp v-bind:num="contexts" v-bind:title="title" v-bind:list="true" v-bind:create_href="create_href"/>
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
              <b-form-select v-model="filter" :options="categories_options"></b-form-select>
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
              <template v-slot:cell(icon)="icon">
                  <span v-html="icon.value"></span>
              </template>
              <template v-slot:cell(category)="data">
                  <router-link class="relation" :to="{ name: 'Category', params: { alias: data.item.category.alias }}">{{data.item.category.name}}</router-link>
              </template>
              <template v-slot:cell(users)="data">
                  <router-link class="relation" :to="{ name: 'MasterEnrol', params: { alias: data.item.alias }}">Matricular</router-link>
              </template>
              <template v-slot:cell(actions)="actions">
                  <span v-html="actions.value"></span>
              </template>
              <template v-slot:cell(name)="data">
                  <router-link :to="{ name: 'Master', params: { alias: data.item.alias }}">{{ data.value }}</router-link>
              </template>
              <template v-slot:cell(actions)="data">
                  <router-link :to="{ name: 'Master', params: { alias: data.item.alias }}"><i class="fas fa-trash-alt"></i></router-link>
                  <router-link :to="{ name: 'Master', params: { alias: data.item.alias }}"><i class="fas fa-cog"></i></router-link>
              </template>
          </b-table>



      </div>
  </div>

</template>

<script>

    import ContainerHeaderApp from '@/layouts/ContainerHeader.vue';
    import {HYP_CONTEXT_MASTER, HYP_CONTEXT_CATEGORY} from '../api/constants';

    export default {
        name: 'Masters',
        components: {
            ContainerHeaderApp
        },
        data() {
            return {
                title: 'Másters',
                contexts: 0,
                create_href: '/masters/_new',
                filter: null,
                categories_options: [],
                fields: [
                    {
                        key: 'state',
                        label: 'Estado',
                        class: 'text-center',
                        sortable: true,
                        formatter: (value) => {
                            switch (value.alias) {
                                case 'active':
                                    return `<i class="fas fa-check-circle"></i>`;
                                case 'unactive':
                                    return `<i class="fas fa-minus-circle"></i>`;
                                case 'finished':
                                    return `<i class="fas fa-flag-checkered"></i>`;
                                case 'creating':
                                    return `<i class="fas fa-pencil-alt"></i>`;
                                case 'paused':
                                    return `<i class="fas fa-pause-circle"></i>`;
                            }
                        }
                    },
                    {
                        key: 'name',
                        label: 'nombre',
                        class: 'text-left',
                        sortable: true
                    },
                    {
                        key: 'alias',
                        label: 'Alias',
                        class: 'text-left',
                        sortable: true
                    },
                    {
                        key: 'created_at',
                        label: 'Creado',
                        class: 'text-left',
                        sortable: true
                    },
                    {
                        key: 'updated_at',
                        label: 'Actualizado',
                        class: 'text-left',
                        sortable: true
                    },
                    {
                        key: 'category',
                        label: 'Categoría',
                        class: 'text-center'
                    },
                    {
                        key: 'users',
                        label: 'Usuarios',
                        class: 'text-center'
                    },
                    {
                        key: 'actions',
                        label: 'Acciones'
                    }
                ],
                items: null
            }
        },
        beforeMount () {
            this.axios
                .get( HYP_CONTEXT_MASTER + '?format=json')
                .then(response => {
                    this.items = response.data;
                    this.contexts = response.data.length;
                });
            this.axios
                .get( HYP_CONTEXT_CATEGORY + 'master/filter/?format=json')
                .then(response => {
                    const data = response.data;
                    const options = [
                        { value: null, text: 'Todas las categorías' }
                    ];

                    data.forEach(element => {
                        let option = {
                            value: element.alias,
                            text: element.name,
                            disabled: element.state.alias !== 'active'
                        };
                        options.push(option);
                    });

                    this.categories_options = options;
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

                i.fas {
                    font-size: 20px;
                    color: #727475;
                    &.fa-check-circle {
                        color: #28BB72;
                    }
                    &.fa-minus-circle {
                        color: #DE8826;
                    }
                    &.fa-flag-checkered {
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

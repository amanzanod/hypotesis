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
              <b-form-select v-model="filter" :options="contexts_options"></b-form-select>
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
              <template v-slot:cell(context_type)="data">
                  {{data.item.context_type.name}}
              </template>
              <template v-slot:cell(actions)="actions">
                  <span v-html="actions.value"></span>
              </template>
              <template v-slot:cell(name)="data">
                  <router-link :to="{ name: 'Category', params: { alias: data.item.alias }}">{{ data.value }}</router-link>
              </template>
              <template v-slot:cell(actions)="data">
                  <router-link :to="{ name: 'Category', params: { alias: data.item.alias }}"><i class="fas fa-trash-alt"></i></router-link>
                  <router-link :to="{ name: 'Category', params: { alias: data.item.alias }}"><i class="fas fa-cog"></i></router-link>
              </template>
          </b-table>

      </div>
  </div>

</template>

<script>

    import ContainerHeaderApp from '@/layouts/ContainerHeader.vue';
    import {HYP_CONTEXT_CATEGORY, HYP_MANAGER_CONTEXT} from '../api/constants';

    export default {
        name: 'Categories',
        components: {
            ContainerHeaderApp
        },
        data() {
            return {
                title: 'Categorías',
                contexts: 0,
                create_href: '/categories/_new',
                filter: null,
                contexts_options: [],
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
                        key: 'context_type',
                        label: 'Contexto',
                        class: 'text-center'
                    },
                    {
                        key: 'parent',
                        label: 'Categoría Padre',
                        class: 'text-center'
                    },
                    {
                        key: 'actions',
                        label: 'Acciones',
                        formatter: (value, key, item) => {
                            let html = ``;
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
                .get( HYP_CONTEXT_CATEGORY + '?format=json')
                .then(response => {
                    this.items = response.data;
                    this.contexts = response.data.length;
                });
            this.axios
                .get( HYP_MANAGER_CONTEXT + '?format=json')
                .then(response => {
                    const data = response.data;
                    const options = [
                        { value: null, text: 'Todas los contextos' }
                    ];

                    data.forEach(element => {
                        let option = {
                            value: element.alias,
                            text: element.name,
                        };
                        options.push(option);
                    });

                    this.contexts_options = options;
                });

        },
        methods: {
            rowClass(item, type) {
                if (!item || type !== 'row') return;
                if (item.is_visible === false) return 'text-muted';
            },
            onFiltered(filteredItems) {
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

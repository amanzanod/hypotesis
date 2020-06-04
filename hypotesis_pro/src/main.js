import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
import VueAxios from 'vue-axios'

import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'


import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import table from 'bootstrap-vue/esm/components/table/table';
import tooltip from 'bootstrap-vue/esm/components/tooltip/tooltip';
import button from 'bootstrap-vue/esm/components/button/button';
import bform from 'bootstrap-vue/esm/components/form/form';
import formgroup from 'bootstrap-vue/esm/components/form-group/form-group';
import formselect from 'bootstrap-vue/esm/components/form-select/form-select';
import forminput from 'bootstrap-vue/esm/components/form-input/form-input';
import inputgroupappend from 'bootstrap-vue/esm/components/input-group/input-group-append';
import bimg from 'bootstrap-vue/esm/components/image/img';



Vue.config.productionTip = false;
Vue.prototype.$menu = {collapsed:false};

// Instal VueAXIOS
Vue.use(VueAxios, axios);
// Install BootstrapVue
Vue.use(BootstrapVue);
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin);

Vue.component('b-table', table);
Vue.component('b-tooltip', tooltip);
Vue.component('b-button', button);
Vue.component('b-form-group', formgroup);
Vue.component('b-form-select', formselect);
Vue.component('b-img', bimg);
Vue.component('b-form', bform);
Vue.component('b-form-input', forminput);
Vue.component('b-input-group-append', inputgroupappend);


new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app');

import Vue from 'vue'
import VueRouter from 'vue-router'
import Users from '../views/Users.vue'

Vue.use(VueRouter);

  const routes = [
  {
    path: '/',
    name: 'Home',
    component: Users
  },
  {
    path: '/users',
    name: 'Users',
    component: Users
  },
  {
    path: '/roles',
    name: 'Roles',
    component: () => import(/* webpackChunkName: "about" */ '../views/Roles.vue')
  }
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
});

export default router

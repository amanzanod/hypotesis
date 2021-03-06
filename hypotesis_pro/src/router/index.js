import Vue from 'vue'
import VueRouter from 'vue-router'
import Users from '../views/Users.vue'

Vue.use(VueRouter);

  const routes = [
  {
      path: '/login',
      name: 'Login',
      component: () => import('../views/Login.vue'),
      meta: 'Iniciar sesión'
  },
  {
      path: '/',
      name: 'Home',
      component: Users,
      meta: 'Inicio'
  },
  {
      path: '/users',
      name: 'Users',
      component: Users,
      meta: 'Usuarios'
  },
  {
      path: '/users/:username',
      name: 'User',
      meta: 'Usuario',
      component: () => import('../views/User.vue'),
      props: true
  },
  {
      path: '/roles',
      name: 'Roles',
      meta: 'Roles',
      component: () => import('../views/Roles.vue')
  },
  {
      path: '/assign_permissions',
      name: 'AssignPermissions',
      meta: 'Asignar Permisos',
      component: () => import('../views/AssignPermissions.vue')
  },
  {
      path: '/roles/:alias',
      name: 'Role',
      meta: 'Rol',
      component: () => import('../views/Role.vue'),
      props: true
  },
  {
      path: '/roles/:alias/permissions',
      name: 'RolePermissions',
      meta: 'Permisos de Rol',
      component: () => import('../views/RolePermissions.vue'),
      props: true
  },
  {
      path: '/roles/:alias/users',
      name: 'RoleUsers',
      meta: 'Usuarios de Rol',
      component: () => import('../views/RoleUsers.vue'),
      props: true
  },
  {
      path: '/permissions',
      name: 'Permissions',
      meta: 'Permisos',
      component: () => import('../views/Permissions.vue')
  },
  {
      path: '/permissions/:alias',
      name: 'Permission',
      meta: 'Permiso',
      component: () => import('../views/Permission.vue'),
      props: true
  },
  {
      path: '/contexts',
      name: 'Contexts',
      meta: 'Contextos',
      component: () => import('../views/Contexts.vue')
  },
  {
      path: '/grades',
      name: 'Grades',
      meta: 'Grados',
      component: () => import('../views/Grades.vue')
  },
  {
      path: '/grades/:alias',
      name: 'Grade',
      meta: 'Grado',
      component: () => import('../views/Grade.vue')
  },
  {
      path: '/masters',
      name: 'Masters',
      meta: 'Másters',
      component: () => import('../views/Masters.vue')
  },
  {
      path: '/masters/:alias',
      name: 'Master',
      meta: 'Máster',
      component: () => import('../views/Master.vue')
  },
  {
      path: '/courses',
      name: 'Courses',
      meta: 'Courses',
      component: () => import('../views/Courses.vue')
  },
  {
      path: '/courses/:alias',
      name: 'Course',
      meta: 'Curso',
      component: () => import('../views/Course.vue')
  },
  {
      path: '/classrooms',
      name: 'Classrooms',
      meta: 'Aulas',
      component: () => import('../views/Classrooms.vue')
  },
  {
      path: '/classrooms/:alias',
      name: 'Classroom',
      meta: 'Aula',
      component: () => import('../views/Classroom.vue')
  },
  {
      path: '/classrooms/:alias/enrol',
      name: 'ClassroomEnrol',
      meta: 'Matriculación en Aula',
      component: () => import('../views/ClassroomEnrol.vue')
  },
  {
      path: '/course/:alias/enrol',
      name: 'CourseEnrol',
      meta: 'Matriculación en Curso',
      component: () => import('../views/CourseEnrol.vue')
  },
  {
      path: '/grade/:alias/enrol',
      name: 'GradeEnrol',
      meta: 'Matriculación en Grado',
      component: () => import('../views/GradeEnrol.vue')
  },
  {
      path: '/master/:alias/enrol',
      name: 'MasterEnrol',
      meta: 'Matriculación en Máster',
      component: () => import('../views/MasterEnrol.vue')
  },
  {
      path: '/categories',
      name: 'Categories',
      meta: 'Categorías',
      component: () => import('../views/Categories.vue')
  },
  {
      path: '/categories/:alias',
      name: 'Category',
      meta: 'Categoría',
      component: () => import('../views/Category.vue')
  },
  {
      path: '/notifications',
      name: 'Notifications',
      meta: 'Notificaciones',
      component: () => import('../views/Notifications.vue')
  },
  {
      path: '/forum',
      name: 'Forum',
      meta: 'Foro',
      component: () => import('../views/Forum.vue')
  },
  {
      path: '/news',
      name: 'News',
      meta: 'Tablón Anuncios',
      component: () => import('../views/News.vue')
  },
  {
      path: '/reports',
      name: 'Reports',
      meta: 'Informes',
      component: () => import('../views/Reports.vue')
  },
  {
      path: '/admin',
      name: 'Admin',
      meta: 'Administración',
      component: () => import('../views/Admin.vue')
  },
  {
      name: '404',
      path: '/*',
      component: () => import('../views/PageNotFound.vue')
  }
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
});

export default router

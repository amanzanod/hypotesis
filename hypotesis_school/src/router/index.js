import Vue from 'vue'
import VueRouter from 'vue-router'

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
      component: () => import('../views/Home.vue'),
      meta: 'Inicio'
  },
  {
      path: '/course_start/:alias',
      name: 'CourseStart',
      component: () => import('../views/CourseStart.vue'),
      meta: 'Portada Curso'
  },
  {
      path: '/course_news/:alias',
      name: 'CourseNews',
      component: () => import('../views/CourseNews.vue'),
      meta: 'Tablón'
  },
  {
      path: '/course_competences/:alias',
      name: 'CourseCompetences',
      component: () => import('../views/CourseCompetences.vue'),
      meta: 'Competencias'
  },
  {
      path: '/course_users/:alias',
      name: 'CourseUsers',
      component: () => import('../views/CourseUsers.vue'),
      meta: 'Participantes'
  },
  {
      path: '/course_itinerary/:alias',
      name: 'CourseItinerary',
      component: () => import('../views/CourseItinerary.vue'),
      meta: 'Itinerario'
  },
  {
      path: '/course_forum/:alias',
      name: 'CourseGrades',
      component: () => import('../views/CourseForum.vue'),
      meta: 'Foro'
  },
  {
      path: '/user_profile',
      name: 'UserProfile',
      component: () => import('../views/UserProfile.vue'),
      meta: 'Perfil'
  },
  {
      path: '/user_courses',
      name: 'UserCourses',
      component: () => import('../views/UserCourses.vue'),
      meta: 'Mis Cursos'
  },
  {
      path: '/user_schedule',
      name: 'UserSchedule',
      component: () => import('../views/UserSchedule.vue'),
      meta: 'Calendario'
  },
  {
      path: '/user_notifications',
      name: 'UserNotifications',
      meta: 'Notificaciones',
      component: () => import('../views/UserNotifications.vue')
  },
  {
      path: '/school_courses',
      name: 'SchoolCourses',
      meta: 'Oferta Cursos',
      component: () => import('../views/SchoolCourses.vue')
  },
  {
      path: '/school_news',
      name: 'SchoolNews',
      meta: 'Noticias',
      component: () => import('../views/SchoolNews.vue')
  },
  {
      path: '/school_forum',
      name: 'SchoolForum',
      meta: 'Foro',
      component: () => import('../views/SchoolForum.vue')
  },
  {
      path: '/school_admin',
      name: 'SchoolAdmin',
      meta: 'Trámites',
      component: () => import('../views/SchoolAdmin.vue')
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

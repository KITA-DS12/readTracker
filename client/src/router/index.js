import { createRouter, createWebHistory } from 'vue-router'
import SignUp from '../views/SignUp.vue'
import SignIn from '../views/SignIn.vue'
import Note from '../views/Note.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'note',
      component: Note
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignUp
    },
    {
      path: '/signin',
      name: 'signin',
      component: SignIn
    },
  ]
})

export default router

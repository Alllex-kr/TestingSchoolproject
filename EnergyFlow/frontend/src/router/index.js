import { createRouter, createWebHistory } from 'vue-router'

import SimulationView from '../views/SimulationView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: SimulationView
    },
   
  ]
})

export default router

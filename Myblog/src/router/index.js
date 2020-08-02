import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/components/Index/Index'
import About from '@/components/About'
import Connect from '@/components/Connect'
import Experience from '@/components/Experience'
import Message from '@/components/Message'
import Mood from '@/components/Mood'
import Recall from '@/components/Recall'
import Technology from '@/components/Technology'
import Detail from '@/components/Detail'
import Register from '@/components/Register'
import Login from '@/components/Login'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'index',
      component: resolve=>(require(["@/components/Index/Index"],resolve))
    },
    {
      path: '/index',
      redirect:'/'
    },
    {
      path: '/about',
      name: 'about',
      component:resolve=>(require(['@/components/About'],resolve))
    },
    {
      path: '/connect',
      name: 'connect',
      component:resolve=>(require(['@/components/Connect'],resolve))
    },
    {
      path: '/experience',
      name: 'experience',
      component:resolve=>(require(['@/components/Experience'],resolve))
    },
    {
      path: '/message',
      name: 'message',
      component:resolve=>(require(['@/components/Message'],resolve))
    },
    {
      path: '/mood',
      name: 'mood',
      component:resolve=>(require(['@/components/Mood'],resolve))
    },
    {
      path: '/recall',
      name: 'recall',
      component:resolve=>(require(['@/components/Recall'],resolve))
    },
    {
      path: '/technology',
      name: 'technology',
      component:resolve=>(require(['@/components/Technology'],resolve))
    },
    {
      path: '/detail/:id',
      name: 'detail',
      component:resolve=>(require(['@/components/Detail'],resolve))
    },
    {
      path: '/register',
      name: 'register',
      component:resolve=>(require(['@/components/Register'],resolve))
    },
    {
      path: '/login',
      name: 'login',
      component:resolve=>(require(['@/components/Login'],resolve))
    },
  ]
})

import Vue from 'vue'
import Router from 'vue-router'
import WebPlayer from '@/components/WebPlayer'
import Home from '@/components/Home'
import YoutubeClassify from '@/components/YoutubeClassify'
Vue.use(Router)

export default new Router({
  routes: [
    {
      // path: '/',
      // name: 'WebPlayer',
      // component: WebPlayer
      //
      // path: '/',
      // name: 'Home',
      // component: Home

      path: '/',
      name: 'YoutubeClassify',
      component: YoutubeClassify
    }
  ]
})

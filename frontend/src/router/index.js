import Vue from 'vue'
import Router from 'vue-router'
import WebPlayer from '@/components/WebPlayer'
import YoutubeClassify from '@/components/YoutubeClassify'
import Stats from '@/components/Stats'
import About from '@/components/About'
import TopSongs from '@/components/TopSongs'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'WebPlayer',
      component: WebPlayer
    },
    {
      path: '/topSongs',
      name: 'topSongs',
      component: TopSongs
    },
    {
      path: '/about',
      name: 'About',
      component: About
    },
    {
      path: '/youtubeClassify',
      name: 'YoutubeClassify',
      component: YoutubeClassify,
    },
    {
      path: '/stats',
      name: 'Stats',
      component: Stats
    }
  ]
})

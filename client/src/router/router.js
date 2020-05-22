import Vue from 'vue'
import Router from 'vue-router'

const Index = () => import('@/page/index.vue');
const ArticleList = () => import('@/page/article/list.vue');

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/admin',
      name: 'Index',
      component: Index,
      children: [
        {
          path: 'article',
          name: 'ArticleList',
          component: ArticleList
        },
      ]
    }
  ]
})

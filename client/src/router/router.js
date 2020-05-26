import Vue from 'vue'
import Router from 'vue-router'

const Index = () => import('@/page/index.vue');
const ArticleList = () => import('@/page/article/list.vue');
const ArticleAdd = () => import('@/page/article/add.vue');

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
        {
          path: 'article/add',
          name: 'ArticleAdd',
          component: ArticleAdd
        },
        {
          path: 'user',
          name: 'ArticleList',
          component: ArticleList
        },
      ]
    },
    {
      path: '*',
      redirect: '/admin/article'
    }
  ]
})

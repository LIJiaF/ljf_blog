import Vue from 'vue'
import Router from 'vue-router'

const Index = () => import('@/page/index.vue');
const ArticleClassList = () => import('@/page/article/class/list.vue');
const ArticleClassAdd = () => import('@/page/article/class/add.vue');
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
          path: 'article/class',
          name: 'ArticleClassList',
          component: ArticleClassList,
          meta: {
            menu: 'article_class'
          }
        },
        {
          path: 'article/class/add',
          name: 'ArticleClassAdd',
          component: ArticleClassAdd,
          meta: {
            menu: 'article_class'
          }
        },
        {
          path: 'article/class/edit/:class_id',
          name: 'ArticleClassEdit',
          props: true,
          component: ArticleClassAdd,
          meta: {
            menu: 'article_class'
          }
        },
        {
          path: 'article',
          name: 'ArticleList',
          component: ArticleList,
          meta: {
            menu: 'article'
          }
        },
        {
          path: 'article/add',
          name: 'ArticleAdd',
          component: ArticleAdd,
          meta: {
            menu: 'article'
          }
        },
        {
          path: 'article/edit/:article_id',
          name: 'ArticleEdit',
          props: true,
          component: ArticleAdd,
          meta: {
            menu: 'article'
          }
        },
        {
          path: 'user',
          name: 'ArticleList',
          component: ArticleList
        },
      ]
    },
    // {
    //   path: '*',
    //   redirect: '/admin/article'
    // }
  ]
})

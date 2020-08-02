// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'

Vue.config.productionTip = false

// 导入element-ui
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
Vue.use(ElementUI)

// 导入最新文章
Vue.component('newarticle', resolve=>(require(['@/components/Public/NewArticle'],resolve)))

// 导入友情链接
Vue.component('friendlylink', resolve=>(require(['@/components/Public/FriendlyLink'],resolve)))

// 导入导航栏下的标题与返回首页
Vue.component('topnav', resolve=>(require(['@/components/Public/TopNav'],resolve)))

// 导入文章列表组件
Vue.component('articlelist', resolve=>(require(['@/components/Public/ArticleList'],resolve)))

// 导入公共文章模板组件
Vue.component('commandmodule', resolve=>(require(['@/components/Public/CommandModule'],resolve)))

// 导入面包屑
Vue.component('breakcrumb', resolve=>(require(['@/components/Public/Breadcrumb'],resolve)))

// 导入声明
Vue.component('announce', resolve=>(require(['@/components/Public/Announce'],resolve)))

// 导入Vuex
import Store from './Store'

// 导入axios
import Axios from 'axios'
Axios.defaults.baseURL = 'http://127.0.0.1:8000/api/'  // 设置默认路劲
Vue.prototype.$axios = Axios  // 全局配置使用

// 时间过滤器
import moment from 'moment'
Vue.filter('timefilter', (data, type)=>{
  return moment(data).format(type)
})

// 字数过滤器
Vue.filter('fontfilter', font=>{
  if (font.length > 100){
    let newfont = font.replace(/&[a-z ]+;/g, '').replace(/<[a-z 1-9=:/;"]+>/g, '').replace(/<p style="text-indent: 2em;">/g, '')
    return newfont.slice(0, 100) + '...'
  }
  return font
})

// 导入分页器
Vue.component('paginator', resolve=>(require(['@/components/Public/Paginator'],resolve)))

// 新建BScroll实例导入上拉和下拉功能
var infiniteScroll =  require('vue-infinite-scroll');
Vue.use(infiniteScroll)

// 全局axios拦截器
import { Loading } from 'element-ui'
import qs from 'qs';
Axios.interceptors.request.use(
  config=>{    
  // 设置加载时候的样式
  Loading.service({text:'玩命加载ing'})
  return config
}, 
  (error)=>{
  return Promise.reject(error)
})

Axios.interceptors.response.use((response)=>{
  Loading.service().close();
  return response
}, (error)=>{
  Loading.service().close();
  return Promise.reject(error)
})

// 导入发送留言框
Vue.component('inputtext', resolve=>(require(['@/components/Public/InputText'],resolve)))

// 导入非登陆禁止留言
Vue.component('needlogin', resolve=>(require(['@/components/Public/NeedLogin'],resolve)))

// 留言版块
Vue.component('discuss', resolve=>(require(['@/components/Public/Discuss'],resolve)))

// 中央事件总线
Vue.prototype.$event = new Vue();

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store:Store,
  components: { App },
  template: '<App/>',
})

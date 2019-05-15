import Vue from 'vue'
import Router from 'vue-router'
import store from '../store'

Vue.use(Router)

var router = new Router({
  // mode:'history',
  routes: [
    {
      path: '/login',
      name: 'login',
      component: () => import('@/views/baseview/login')
    },
    {
      path: '/register',
      name: 'register',
      component: () => import('@/views/baseview/register')
    },
    // {
    //   path: '/useraccount',
    //   name: 'useraccount',
    //   component: () => import('@/views/baseview/useraccount')
    // },
    {
      path: '/chating',
      name: 'chating',
      component: () => import('@/views/baseview/chating'),
    },
    {
      path: '/friendinfoview',
      name: 'friendinfoview',
      component: () => import('@/views/baseview/friendinfoview'),
    },
    {
      path: '/addfriend',
      name: 'addfriend',
      component: () => import('@/views/baseview/addfriend'),
    },
    {
      path: '/addfriendtrue',
      name: 'addfriendtrue',
      component: () => import('@/views/baseview/addfriend_true'),
    },
    {
      path: '/addfriendagree',
      name: 'addfriendagree',
      component: () => import('@/views/baseview/addfriend_agree'),
    },
    {
      path: '/',
      name: 'chatbase',
      redirect: '/chatview',
      component: () => import('@/views/baseview/ChatBase'),
      children: [
        {
          path: 'chatview',
          name: 'chatview',
          component: () => import('@/views/baseview/chatview'),
        },
        {
          path: 'friendsview',
          name: 'friendsview',
          component: () => import('@/views/baseview/friendsview'),
        },
        {
          path: 'userinfoview',
          name: 'userinfoview',
          component: () => import('@/views/baseview/userinfoview'),
        }
      ]
    }
  ]
})

const whiteList = ['/login','/register']  // 路由白名单，不需要登录的路由放在这里面
// ,'/','/chatview','/friendsview','/chating','/userinfoview','/friendinfoview','/addfriend','/addfriendtrue','/addfriendagree'
// const router_list = ['/register']
// // 路由判断。登录验证,如果没有登录，就全部定向到login界面。token就正常访问
router.beforeEach((to,from,next) => {
//   window.addEventListener('load',function () {
//     // console.log('测试会不会出现')
//     console.log(from.path)
//     console.log(to.path)
//     if (router_list.indexOf(to.path) !== -1) {
//       // console.log('测试会不会出现')
//       next({ path: '/logoin' })
//     }
//   })
  if (store.state.user_token) {
    if (to.path === '/login' || to.path === '/register') { // 如果当前用户输入的是登录路由，那么就定向到 /useraccount 路由
      next('/userinfoview')
    } else {
      if (!store.state.nickname) { // 判断用户信息是否存在，不存在就拉取用户信息
        store.dispatch('GetInfo').then(res => { // 拉取用户信息
          next()
        }).catch((err) => {
          store.dispatch('FedLogOut').then(() => {  // 发生错误就直接清除token，重新登录
            next({ path: '/login' })
          })
        })
      } else {
        next()
      }
    }
  } else {
    if (whiteList.indexOf(to.path) !== -1) {
      next()
    } else {
      next('/login')
    }
  }
})

export default router

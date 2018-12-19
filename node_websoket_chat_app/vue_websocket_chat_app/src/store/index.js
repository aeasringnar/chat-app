import Vue from 'vue'
import vuex from 'vuex'
// import Cookies from 'js-cookie'
import { login, logout, getInfo } from '@/api/chat'
// import { getToken, setToken, removeToken, setsession, getsession, removesession } from '@/utils/user'

Vue.use(vuex);

//state为访问状态对象 数字常量等
const state = {
  x:5,
  user_token: localStorage.getItem('ChatUserToken'),
  user_id: localStorage.getItem('ChatUserId'),
  user_account: localStorage.getItem('ChatUserAccount'),
  nickname: localStorage.getItem('ChatUserNickname'),
  all_mag_data: [],
  all_add_msg_data: []
};
//访问触发状态mutation是同步的
//actions是异步的
const mutations = {
  SET_USER_TOKEN: (state, token) => {
    state.user_token = token
  },
  SET_NICK_NAME: (state, nickname) => {
    state.nickname = nickname
  },
  SET_USER_ACCOUNT: (state, account) => {
    state.user_account = account
  },
  SET_USER_ID: (state, id) => {
    state.user_id = id
  },
  SET_MSG_DATA: (state, arr) => {
    state.all_mag_data = arr
  },
  SET_ADD_MSG_DATA: (state, arr) => {
    state.all_add_msg_data = arr
  },
};
const actions = {
  Login({ commit }, userInfo) {
    return new Promise((resolve, reject) => {
      login(userInfo.username, userInfo.password).then(response => {
        const data = response.data
        localStorage.setItem('ChatUserToken',data.token)
        commit('SET_USER_TOKEN', data.token)
        resolve()
      }).catch(error => {
        console.log()
        reject(error)
      })
    })
  },
  GetInfo({ commit }) {
    return new Promise((resolve, reject) => {
      getInfo().then(response => {
        const data = response.data
        console.log(data)
        localStorage.setItem('ChatUserId',data.id)
        localStorage.setItem('ChatUserNickname',data.nickname)
        localStorage.setItem('ChatUserAccount',data.user_account)
        commit('SET_NICK_NAME', data.nickname)
        commit('SET_USER_ACCOUNT', data.user_account)
        commit('SET_USER_ID', data.id)
        resolve()
      }).catch(error => {
        console.log(error)
      })
    })
  },
  // 前端 登出
  FedLogOut({ commit }) {
    return new Promise(resolve => {
      logout().then(response => {
        const data = response.data
        console.log(data)
        console.log('开始清空数据')
        localStorage.removeItem('ChatUserToken')
        localStorage.removeItem('ChatUserId')
        localStorage.removeItem('ChatUserAccount')
        localStorage.removeItem('ChatUserNickname')
        commit('SET_USER_TOKEN', '')
        commit('SET_NICK_NAME', '')
        commit('SET_USER_ACCOUNT', '')
        commit('SET_USER_ID', '')
        commit('SET_MSG_DATA', [])
        commit('SET_ADD_MSG_DATA', [])
        resolve()
      }).catch(error => {
        console.log(error)
      })
    })
  }
};

//getters 类似于生命周期里面的钩子，getters是在页面刚刚加载完毕之后马上加载，类似于生命周期里面的created
const getters = {
  x: state => state.x + 200,
};
export default new vuex.Store({
  state,
  mutations,
  getters,
  actions
})

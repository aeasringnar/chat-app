import request from '@/utils/request'
// import { login, getInfo, register, logout, getUserfriends, getFriendInfo, getFriendInfo, addFriend } from '@/api/chat'

// 登录
export function login(username, password) {
  return request({
    url: '/chat/login',
    method: 'post',
    data: {
      username,
      password
    }
  })
}

// 注册
export function register(data) {
  return request({
    url: '/chat/register',
    method: 'post',
    data: data
  })
}

// 获取用户信息
export function getInfo() {
  return request({
    url: '/chat/userinfo',
    method: 'get',
  })
}

// 登出
export function logout() {
  return request({
    url: '/chat/logout',
    method: 'get'
  })
}

// 获取用户好友列表
export function getUserfriends() {
    return request({
      url: '/chat/userfriends',
      method: 'get',
    })
}

// 获取好友信息
export function getFriendInfo(friend_id) {
    return request({
      url: '/chat/friendinfo',
      method: 'get',
      params: {
          friend_id
      }
    })
}

// 添加好友
export function addFriend(data) {
    return request({
      url: '/chat/addfriend',
      method: 'post',
      data: data
    })
}

// 搜索好友信息
export function findFriendInfo(keyword) {
    return request({
      url: '/chat/findfriend',
      method: 'get',
      params: {
        keyword
      }
    })
}
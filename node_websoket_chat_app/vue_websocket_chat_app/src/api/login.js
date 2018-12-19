import request from '@/utils/request'

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

export function register(username, password, captcha) {
  return request({
    url: '/chat/register',
    method: 'post',
    data: {
      username,
      password,
      captcha
    }
  })
}

export function getInfo() {
  return request({
    url: '/chat/userinfo',
    method: 'get'
  })
}

export function logout() {
  return request({
    url: '/chat/logout',
    method: 'get'
  })
}

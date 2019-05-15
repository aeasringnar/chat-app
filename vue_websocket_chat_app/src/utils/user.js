import Cookies from 'js-cookie'

const TokenKey = 'Base-Token'

export function getToken() {
  return Cookies.get(TokenKey)
}

export function setToken(token) {
  return Cookies.set(TokenKey, token)
}

export function removeToken() {
  return Cookies.remove(TokenKey)
}

const SessionKey = 'UserToken'
export function setsession(token) {
  return localStorage.setItem(SessionKey,token)
}

export function getsession() {
  return localStorage.getItem(SessionKey)
}

export function removesession() {
  return localStorage.removeItem(SessionKey)
}
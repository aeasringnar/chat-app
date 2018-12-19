
var service = require("./axios_http")

function getuserinfo() {
    return service.service({
      url: '/account/userinfo',
      method: 'get'
    })
  }
function login(username,password) {
    return service.service({
        url: '/account/login',
        method: 'post',
        data: {
            username,
            password
        }
    })
  }
function getuserinfo_data() {
    getuserinfo().then(response => {
        var data = response.data
        console.log(data)
    }).catch(error => {
        console.log(error)
    })
}
function login_data(username,password) {
    login(username,password).then(response => {
        var data = response.data
        console.log(data)
    }).catch(error => {
        console.log(error)
    })
}
// getuserinfo_data()
login_data('admin','123456')

module.exports = {
    getuserinfo_data,
    login_data
  }
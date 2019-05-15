<template>
    <div class="icontent">
        <div class="logincontent">
            <h3>登录</h3>
            <input type="text" v-model="login_form.username" placeholder="请输入账号或手机号">
            <input type="password" v-model="login_form.password" placeholder="请输入密码">
            <div class="loginb_div">
                <div class="loginb" @click="loginb($event)">登录</div>
                <div class="registerb" @click="register($event)">注册</div>
            </div>
        </div>
    </div>
</template>

<script>
    import store from '@/store'
    import Vue from 'vue'
    import { login, getInfo, register, logout, getUserfriends, getFriendInfo, addFriend } from '@/api/chat'

    export default {
        name: "login",
        data () {
            return {
                login_form: {
                    username: '',
                    password: ''},
            }
        },
        methods: {
            get_userinfo() {
                getInfo().then(response => {
                    const data = response.data
                    console.log(data)
                }).catch(error => {
                    alert(error)
                })
            },
            get_websocket(user_id) {
                /*创建socket连接*/
                var socket = new WebSocket("ws://127.0.0.1:8801");
                socket.onopen = function (e) {
                    console.log('WebSocket open!');//成功连接上Websocket
                    var msg_obj = {
                        'msg_type':3,
                        'msg':'login',
                        'token':'123456',
                        'user_id':user_id,
                        'nickname':'test',
                        'friend_id':0
                        }
                    socket.send(JSON.stringify(msg_obj))
                };
                // 监听消息
                socket.onmessage = function (e) {
                    console.log('message: ' + e.data);//打印出服务端返回过来的数据
                    var msg_obj = JSON.parse(e.data)
                    if (msg_obj.msg != '登录成功') {
                        // 监听好友消息
                        if(msg_obj.msg_type == 1) {
                            var data_index = -1
                            for(var i in store.state.all_mag_data) {
                                console.log('开始循环查找...')
                                if(store.state.all_mag_data[i].friend_id == msg_obj.user_id) {
                                    data_index = i
                                }
                            }
                            console.log("找到的index:",data_index)
                            if(data_index == -1) {
                                var msg_item = {
                                    friend_id: msg_obj.user_id,
                                    nickname: msg_obj.nickname,
                                    friend_url: '',
                                    msg_data: []
                                }
                                msg_item.msg_data.push(msg_obj)
                                store.state.all_mag_data.push(msg_item)
                            } else {
                                store.state.all_mag_data[data_index].msg_data.push(msg_obj)
                            }
                        } else if(msg_obj.msg_type == 2) {
                            // 监听添加好友消息
                            store.state.all_add_msg_data.push(msg_obj)
                        }
                    }
                };
                socket.onerror = function(e) { // 绑定链接错误事件
                    console.log(e);
                    alert('websocket服务端未开启或发生错误，无法链接！')
                };
                window.s = socket;
            },
            loginb(e) {
                if (this.login_form.username === '' || this.login_form.password === '') {
                    alert('用户名或密码不能为空！')
                } else {
                    this.$store.dispatch('Login', this.login_form).then(() => {
                        console.log('登录成功')
                        // this.get_userinfo()
                        this.$store.dispatch('GetInfo').then(() => {
                            console.log('获取用户信息成功')
                            this.get_websocket(store.state.user_id)
                            this.$router.push({ name: 'chatview'})
                        }).catch((error) => {
                            alert(error)
                        })
                    }).catch((error) => {
                        alert(error)
                    })
                }
            },
            register () {
                this.$router.push({ name: 'register'})
            }
        },
        created: function() {
        }
    }
</script>

<style scoped>
    .icontent{
        width: 90%;
        height: 100%;
        margin: 0 5% 0 5%;
        overflow: hidden;
    }
    .logincontent{
        width: 90%;
        height: 100%;
        margin: 50px 5% 0 5%;
        overflow: hidden;
        text-align: center;
    }
    .logincontent input{
        text-align: center;
        display: block;
        width: 400px;
        height: 35px;
        padding: 3px;
        margin: 20px calc(50% - 200px) 20px calc(50% - 200px);
        background:none;  
        outline:none;  
        border:0px;
        border-bottom: 2px solid #dcdcdc;
        border-bottom-left-radius: 1px;
        border-bottom-right-radius: 1px;
        box-sizing: border-box;
        font-family: PingFangSC-Regular;
        font-size: 16px;
    }
    .logincontent input:focus{
        border-bottom: 2px solid #0F996B;
        border-bottom-left-radius: 1px;
        border-bottom-right-radius: 1px;
        /* box-shadow: 0 0 5px #66AACC; */
        /* outline: none; */
    }
    .loginb_div{
        overflow: hidden;
        width: 100%;
        text-align: center;
    }
    .loginb{
        /* float: right; */
        display: inline-block;
        width: 200px;
        height: 40px;
        line-height: 40px;
        background-color: rgb(7, 187, 127);
        border-radius: 5px;
        font-size: 18px;
        font-family: PingFangSC-Regular;
        color: #ffffff;
        margin: 0 0 20px 0;
    }
    .loginb:active{
        background-color: #0F996B;
    }
    .loginb:hover{
        cursor: pointer;
    }
    .registerb{
        /* float: left; */
        display: inline-block;
        width: 200px;
        height: 40px;
        line-height: 40px;
        background-color: rgb(7, 187, 127);
        border-radius: 5px;
        font-size: 18px;
        font-family: PingFangSC-Regular;
        color: #ffffff;
    }
    .registerb:active{
        background-color: #0F996B;
    }
    .registerb:hover{
        cursor: pointer;
    }
</style>
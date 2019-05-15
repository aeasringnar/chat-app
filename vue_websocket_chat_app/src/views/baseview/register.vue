<template>
    <div class="icontent">
        <div class="logincontent">
            <h3>Rgeister 注册</h3>
            <input type="text" v-model="login_form.nickname" placeholder="请输入昵称">
            <input type="text" v-model="login_form.phone" placeholder="请输入手机号">
            <input type="password" v-model="login_form.password" placeholder="请输入密码">
            <div class="loginb_div">
                <div class="registerb" @click="register($event)">注册</div>
                <div class="loginb" @click="backb($event)">返回</div>
            </div>
        </div>
    </div>
</template>

<script>
    import { login, getInfo, register, logout, getUserfriends, getFriendInfo, addFriend } from '@/api/chat'
    import store from '@/store'
    import Vue from 'vue'

    export default {
        name: "register",
        data () {
            return {
                login_form: {
                    phone: '',
                    password: '',
                    nickname: ''},
            }
        },
        methods: {
            register(e) {
                // this.$router.push({ name: 'cousermanager', params: { pagenum: pagenum }})
                // this.$router.push({ name: 'groupwork'})
                if (this.login_form.username === '' || this.login_form.password === '' || this.login_form.nickname === '') {
                    alert('手机号或密码或昵称不能为空！')
                } else {
                    register(this.login_form).then(response => {
                        const data = response.data
                        console.log(data)
                        console.log('成功')
                        var str = '注册成功，账号为：' + String(data.user_account) + ',您可以使用账号或手机号或昵称进行登录!'
                        alert(str)
                        this.$router.push({ name: 'login'})
                    }).catch(error => {
                        console.log('有错误发生')
                        console.log(error)
                        alert(error)
                    })
                }
            },
            backb () {
                this.$router.push({ name: 'login'})
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
    }
    .loginb_div{
        overflow: hidden;
        width: 100%;
        text-align: center;
    }
    .loginb{
        display: inline-block;
        width: 190px;
        height: 40px;
        line-height: 40px;
        background-color: rgb(7, 187, 127);
        border-radius: 5px;
        font-size: 18px;
        font-family: PingFangSC-Regular;
        color: #ffffff;
    }
    .loginb:active{
        background-color: #0F996B;
    }
    .loginb:hover{
        cursor: pointer;
    }
    .registerb{
        display: inline-block;
        width: 190px;
        height: 40px;
        line-height: 40px;
        background-color: rgb(7, 187, 127);
        border-radius: 5px;
        font-size: 18px;
        font-family: PingFangSC-Regular;
        color: #ffffff;
        margin: 0 0 20px 0;
    }
    .registerb:active{
        background-color: #0F996B;
    }
    .registerb:hover{
        cursor: pointer;
    }
</style>
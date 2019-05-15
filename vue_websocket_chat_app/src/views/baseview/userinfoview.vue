<template>
    <div class="icontent">
        <div class="iheader">
            <div class="ititle">用户信息</div>
            <div class="usericon"><img src="../../static/icon/icon-login@3x.png" alt="用户头像"></div>
        </div>
        <div class="icontainr">
            <ul>
                <li>账号：{{user_data.user_account}}</li>
                <li>昵称：{{user_data.nickname}}</li>
                <li>手机：{{user_data.phone}}</li>
                <li>邮箱：{{user_data.email}}</li>
                <li @click="logo_out">退出登录</li>
            </ul>
        </div>
    </div>
</template>

<script>
    import Vue from 'vue'
    import store from '@/store'
    import { login, getInfo, register, logout, getUserfriends, getFriendInfo, addFriend } from '@/api/chat'

    export default {
        name: "userinfoview",
        data () {
            return {
                msg: 'userinfoview',
                user_data: {},
            }
        },
        methods: {
            get_userinfo() {
                getInfo().then(response => {
                    const data = response.data
                    console.log(data)
                    this.user_data = data
                }).catch(error => {
                    alert(error)
                })
            },
            logo_out () {
                this.$store.dispatch('FedLogOut').then(() => {
                    console.log('退出登录成功!')
                    window.s.close()
                    this.$router.push({ name: 'login'})
                }).catch((error) => {
                    console.log(error)
                })
            }
        },
        created: function() {
            this.get_userinfo()
        }
    }
</script>

<style scoped>
    .icontent{
        width: 100%;
        overflow: hidden;
    }
    .iheader{
        width: 100%;
        height: 44px;
        position: relative;
        overflow: hidden;
        background-color:  #FFFFFF;
        border-bottom: 1px solid #DCDCDC;
    }
    .toback{
        float: left;
        width: 20px;
        height: 20px;
        margin-top: 12px;
        margin-left: 16px;
    }
    .toback:hover{
        cursor: pointer;
    }
    .toback img{
        height: 100%;
    }
    .ititle{
        float: left;
        height: 16px;
        width: 200px;
        font-size: 14px;
        color: #323A45;
        line-height: 16px;
        margin-top: 14px;
        margin-left: 20px;
    }
    .usericon{
        float: right;
        height: 20px;
        width: 20px;
        border-radius: 10px;
        margin-top: 13px;
        margin-right: 20px;
    }
    .usericon img{
        width: 100%;
    }
    .icontainr{
        height: 100%;
        width: 100%;
    }
    .icontainr ul{
        list-style: none;
        padding: 0;
        margin: 0;
    }
    .icontainr ul li{
        line-height: 50px;
        height: 50px;
        font-size: 14px;
        color: #323A45;
        margin-top: 10px;
        padding-left: 20px;
        background-color: #F5F5F5;
    }
    .icontainr ul li:last-child{
        padding: 0;
        text-align: center;
    }
    .icontainr ul li:last-child:hover{
        cursor: pointer;
    }
</style>
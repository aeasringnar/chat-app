<template>
    <div class="icontent">
        <div class="iheader">
            <div class="ititle">用户信息</div>
            <div class="usericon"><img src="../../static/icon/icon-login@3x.png" alt="用户头像"></div>
        </div>
        <div class="icontainr">
            <ul>
                <li>姓名 Name：{{user_data.name}}</li>
                <li>性别 Gender：{{user_data.gender}}</li>
                <li>手机号 Phone：{{user_data.phone}}</li>
                <li>邮箱 Email：{{user_data.email}}</li>
                <li @click="logo_out">退出登录 Logout</li>
            </ul>
        </div>
    </div>
</template>

<script>
    // import upicon from '../../static/icon/icon-up@3x.png'
    // import downicon from '../../static/icon/icon-down@3x.png'
    // import $ from 'jquery'
    // $(function () {
    //     $('.itab ul li').click(function () {
    //         // console.log('okkk')
    //         // var index = $(this).index()
    //         var all_li = $(this).parent().children()
    //         // console.log(all_li)
    //         var len = all_li.length
    //         for(var i=0;i<len;i++){
    //             $(all_li[i]).children().removeClass('havecolor')
    //         }
    //         // console.log($(this).children())
    //         $(this).children().addClass('havecolor')
    //     })
    // })
    import Vue from 'vue';
    import { login, getInfo, register, logout, getUserfriends, getFriendInfo, addFriend } from '@/api/chat'

    export default {
        name: "useraccount",
        data () {
            return {
                user_data: {}
            }
        },
        methods: {
            getuserinfo () {
                getInfo().then(response => {
                    var data = response.data
                    switch (data.gender) {
                        case 0:
                            data.gender = '男'
                            break
                        case 1:
                            data.gender = '女'
                            break
                        case 2:
                            data.gender = '保密'
                            break
                        case 3:
                            data.gender = '未设置'
                            break
                        default:
                            data.gender = '未设置'
                    }
                    // console.log(data)
                    this.user_data = data
                }).catch(error => {
                    console.log(error)
                })
            },
            logo_out () {
                this.$store.dispatch('FedLogOut').then(() => {
                    console.log('退出登录成功')
                    this.$router.push({ name: 'login'})
                }).catch(() => {
                    console.log('error')
                })
            }
        },
        created: function() {
            this.getuserinfo()
        }
    }
</script>

<style scoped>
    body{
        background-color: #F5F5F5 !important;
    }
    .icontent{
        width: 40%;
        margin: 0 30% 0 30%;
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
        width: 260px;
        font-size: 14px;
        color: #323A45;
        line-height: 16px;
        margin-top: 14px;
        /* margin-left: 20px; */
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
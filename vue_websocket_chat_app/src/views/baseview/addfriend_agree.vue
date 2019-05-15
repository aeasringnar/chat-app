<template>
    <div class="icontent">
        <div>
            <mu-appbar style="width: 100%;height: 50px;" color="primary">
                <mu-button icon slot="left" @click="to_back">
                    <mu-icon value="keyboard_arrow_left"></mu-icon>
                </mu-button>
                <mu-button flat slot="right">
                    <!-- <mu-icon size="32" value="add"></mu-icon> -->
                </mu-button>
            </mu-appbar>
        </div>
        <div class="iheader">
            <div class="ititle">对方信息</div>
            <div class="usericon"><img src="../../static/icon/icon-login@3x.png" alt="用户头像"></div>
        </div>
        <div class="icontainr">
            <ul>
                <li>账号：{{user_data.user_account}}</li>
                <li>昵称：{{user_data.nickname}}</li>
                <li>手机：{{user_data.phone}}</li>
                <li>邮箱：{{user_data.email}}</li>
            </ul>
        </div>
        <div class="bot_content_out">
            <div class="bot_content">
                <div class="notagree">拒绝</div>
                <div class="loginb" @click="agree(user_data.id)">同意</div>
            </div>
        </div>
    </div>
</template>

<script>
    import Vue from 'vue'
    import store from '@/store'
    import { login, getInfo, register, logout, getUserfriends, getFriendInfo, addFriend } from '@/api/chat'

    export default {
        name: "addfriend_agree",
        data () {
            return {
                user_data: {},
            }
        },
        methods: {
            get_friendinfo(friend_id) {
                getFriendInfo(friend_id).then(response => {
                    const data = response.data
                    console.log(data)
                    this.user_data = data
                }).catch(error => {
                    alert(error)
                })
            },
            add_friend(data) {
                addFriend(data).then(response => {
                    const data = response.data
                    console.log(data)
                    alert('添加成功')
                    this.$router.push({ name: 'friendsview'})
                }).catch(error => {
                    alert(error)
                })
            },
            to_back(){
                this.$router.go(-1)
            },
            agree(id) {
                console.log(id)
                var data = {
                    friend_id: id
                }
                this.add_friend(data)
            }
        },
        created: function() {
            // this.$route.params.friend_id
            this.get_friendinfo(this.$route.params.friend_id)
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
    .bot_content_out{
        overflow: hidden;
        width: 100%;
        text-align: center;
    }
    .bot_content{
        overflow: hidden;
        display: inline-block;
    }
    .notagree{
        float: left;
        width: 60px;
        height: 40px;
        line-height: 40px;
        background-color: rgb(7, 187, 127);
        border-radius: 5px;
        font-size: 18px;
        font-family: PingFangSC-Regular;
        color: #ffffff;
        margin: 20px 10px 20px 10px;
        text-align: center;
    }
    .loginb{
        float: left;
        width: 60px;
        height: 40px;
        line-height: 40px;
        background-color: rgb(7, 187, 127);
        border-radius: 5px;
        font-size: 18px;
        font-family: PingFangSC-Regular;
        color: #ffffff;
        margin: 20px 10px 20px 10px;
        text-align: center;
    }
    .loginb:active{
        background-color: #0F996B;
    }
    .loginb:hover{
        cursor: pointer;
    }
    .notagree:active{
        background-color: #0F996B;
    }
    .notagree:hover{
        cursor: pointer;
    }
</style>
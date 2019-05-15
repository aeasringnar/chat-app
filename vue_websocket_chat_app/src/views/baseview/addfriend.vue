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
        <div class="my-chat-input">
            <textarea v-model='search_txt' placeholder="请输入账号或昵称"></textarea>
            <div class="my-chat-botton" @click="to_find">搜索</div>
        </div>
        <div class="my-chat-item" v-for="data in user_data_list" @click="to_friendtrue(data)">
            <div class="my-chat-ico">
                <img src="../../static/icon/icon-login@3x.png" alt="用户头像">
            </div>
            <div class="my-chat-msg">
                <div class="my-chat-msg-top">{{ data.nickname }}</div>
                <div class="my-chat-msg-bot">{{ data.user_account }}</div>
            </div>
        </div>
    </div>
</template>

<script>
    import Vue from 'vue'
    import store from '@/store'
    import { login, getInfo, register, logout, getUserfriends, getFriendInfo, addFriend, findFriendInfo } from '@/api/chat'

    export default {
        name: "addfriend",
        data () {
            return {
                msg: 'addfriend',
                search_txt: '',
                user_data_list: []
            }
        },
        methods: {
            find_friend(keyword) {
                findFriendInfo(keyword).then(response => {
                    const data = response.data
                    console.log(data)
                    this.user_data_list = data
                }).catch(error => {
                    alert(error)
                })
            },
            to_find() {
                this.find_friend(this.search_txt)
            },
            to_back(){
                this.$router.go(-1)
            },
            to_friendtrue(data) {
                this.$router.push({ name: 'addfriendtrue',params:{ add_friend_data: data }})
            }
        },
        created: function() {
        }
    }
</script>

<style scoped>
    .icontent{
        width: 100%;
        overflow: hidden;
    }
    .my-chat-input{
        overflow: hidden;
        margin: 0;
        padding: 0;
        height: 40px;
        width: 100%;
        border-bottom: 1px solid gainsboro;
    }
    .my-chat-input textarea{
        width: calc(100% - 75px);
        height: 30px;
        padding: 5px;
        resize:none;
        border: 1px solid #DCDCDC;
        border-radius: 4px;
        background:none;  
        outline:none; 
        font-size: 14px;
        margin: 0;
        margin: 5px 0 0 5px;
    }
    .my-chat-input textarea::-webkit-scrollbar {
        display: none;
    }
    .my-chat-input textarea:focus{
        border: 1px solid rgb(7, 187, 127);
        border-radius: 4px;
    }
    .my-chat-botton{
        float: right;
        text-align: center;
        width: 60px;
        height: 30px;
        font-size: 18px;
        line-height: 30px;
        background-color: rgb(7, 187, 127);
        color: white;
        border-radius: 4px;
        margin: 5px 5px 0 0;
    }
    .my-chat-botton:active{
        background-color: #0F996B;
    }
    .my-chat-botton:hover{
        cursor: pointer;
    }
    .my-chat-item{
        height: 51px;
        width: 100%;
        /* background-color: brown; */
        padding: 5px;
        border-bottom: 1px solid gainsboro;
        overflow: hidden;
    }
    .my-chat-ico{
        width: 40px;
        height: 40px;
        float: left;
        position: relative;
    }
    .my-chat-ico img{
        width: 100%;
        height: 100%;
        position: absolute;
        top: 0;
        left: 0;
    }
    .my-chat-msg{
        float: left;
        width: calac(100% - 40px);
        height: 40px;
        /* background-color: aquamarine; */
        padding: 0 5px 0 5px; 
        overflow: hidden;
    }
    .my-chat-msg-top{
        width: 100%;
        height: 22px;
        overflow: hidden;
        font-size: 18px;
        line-height: 22px;
    }
    .my-chat-msg-bot{
        width: 100%;
        height: 18px;
        overflow: hidden;
        font-size: 14px;
        line-height: 18px;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
    }
</style>
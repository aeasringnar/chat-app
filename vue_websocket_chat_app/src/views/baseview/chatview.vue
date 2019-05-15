<template>
    <div class="icontent">
        <div class="my-chat-item" v-for="msg_item in $store.state.all_mag_data" @click="to_chating(msg_item.friend_id,msg_item.nickname)">
            <div class="my-chat-ico">
                <img src="../../static/icon/icon-login@3x.png" alt="用户头像">
            </div>
            <div class="my-chat-msg">
                <div class="my-chat-msg-top">{{ msg_item.nickname }}</div>
                <div class="my-chat-msg-bot">{{ msg_item.msg_data[msg_item.msg_data.length-1].msg }}</div>
            </div>
            <div class="my-ms-right">
                <div class="my-ms-fight-left"></div>
                <div class="my-ms-fight-right"></div>
            </div>
        </div>
        <div class="my-chat-item" v-for="add_msg in $store.state.all_add_msg_data" @click="to_addfriendagree(add_msg.user_id)">
            <div class="my-chat-ico">
                <img src="../../static/icon/icon-login@3x.png" alt="用户头像">
            </div>
            <div class="my-chat-msg">
                <div class="my-chat-msg-top">{{ add_msg.nickname }}</div>
                <div class="my-chat-msg-bot add_friend">请求添加好友!</div>
            </div>
            <div class="my-ms-right">
                <div class="my-ms-fight-left"></div>
                <div class="my-ms-fight-right"></div>
            </div>
        </div>
    </div>
</template>

<script>
    import Vue from 'vue'
    import { login, getInfo, register, logout, getUserfriends, getFriendInfo, addFriend } from '@/api/chat'
    import store from '@/store'

    export default {
        name: "chatview",
        data () {
            return {
                msg: 'chatview'
            }
        },
        methods: {
            to_chating(id) {
                this.$router.push({ name: 'chating',params:{ friend_id: id }})
            },
            to_addfriendagree(id,nickname) {
                this.$router.push({ name: 'addfriendagree',params:{ friend_id: id, nickname: nickname }})
            }
        },
        created: function() {
            // console.log(store.state.user_token)
        }
    }
</script>

<style scoped>
    .icontent{
        width: 100%;
        overflow: hidden;
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
        width: calc(100% - 100px);
        height: 40px;
        /* background-color: aquamarine; */
        padding: 0 5px 0 5px; 
        overflow: hidden;
    }
    .my-ms-right{
        float: left;
        width: 60px;
        height: 40px;
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
    .my-ms-fight-left{
        width: 100%;
        height: 20px;
        text-align: center;
        line-height: 20px;
    }
    .my-ms-fight-right{
        width: 100%;
        height: 20px;
        text-align: center;
        line-height: 20px;
    }
    .add_friend{
        color: rgb(7, 187, 127);
    }
</style>
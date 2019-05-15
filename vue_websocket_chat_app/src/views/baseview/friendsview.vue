<template>
    <div class="icontent">
        <div class="my-chat-item" v-for="data in friends_list" @click="to_friendinfo(data.friend.id)">
            <div class="my-chat-ico">
                <img src="../../static/icon/icon-login@3x.png" alt="用户头像">
            </div>
            <div class="my-chat-name">
                {{ data.friend.nickname }}
            </div>
        </div>
    </div>
</template>

<script>
    import Vue from 'vue'
    import store from '@/store'
    import { login, getInfo, register, logout, getUserfriends, getFriendInfo, addFriend } from '@/api/chat'

    export default {
        name: "friendsview",
        data () {
            return {
                msg: 'friendsview',
                friends_list: [],
            }
        },
        methods: {
            get_friends() {
                getUserfriends().then(response => {
                    const data = response.data
                    console.log(data)
                    this.friends_list = data
                }).catch(error => {
                    alert(error)
                })
            },
            to_friendinfo(id) {
                this.$router.push({ name: 'friendinfoview', params:{ friend_id: id }})
            }
        },
        created: function() {
            this.get_friends()
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
    .my-chat-item:hover{
        cursor: pointer;
    }
    .my-chat-ico{
        width: 40px;
        height: 40px;
        float: left;
    }
    .my-chat-ico img{
        width: 100%;
        height: 100%;
    }
    .my-chat-name{
        float: left;
        width: calc(100% - 40px);
        height: 40px;
        padding: 0 5px 0 5px; 
        overflow: hidden;
        line-height: 40px;
        font-size: 18px;
    }
</style>
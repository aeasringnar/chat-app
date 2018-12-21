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
        <div class="my-chating-content">
            <div class="my-chating-show" id="words">
                <div v-for="msg_item in $store.state.all_mag_data"
                    v-if="msg_item.friend_id == friend_id">
                    <div v-for="i in msg_item.msg_data" 
                    :class="i.user_id == $store.state.user_id ?'btalk':'atalk'">
                        <span>{{ i.msg }}</span>
                    </div>
                </div>
            </div>
            <div class="my-chating-input"></div>
        </div>
        <div class="my-chat-input">
            <textarea v-model='send_msg'></textarea>
            <div class="my-chat-botton" @click="send_data">发送</div>
        </div>
    </div>
</template>

<script>
    import store from '@/store'
    import { login, getInfo, register, logout, getUserfriends, getFriendInfo, addFriend } from '@/api/chat'
    import Vue from 'vue'
    import $ from 'jquery'
    export default {
        name: "chating",
        data () {
            return {
                msg: 'chating',
                send_msg:'',
                friend_id: this.$route.params.friend_id,
                nickname: this.$route.params.nickname
            }
        },
        methods: {
            send_data: function(){
                if(this.send_msg == ''){
                    alert('请输入消息内容...')
                    return;
                }
                console.log(store.state.user_id)
                console.log(store.state.nickname)
                var msg_obj = {
                    'msg_type':1,
                    'msg':this.send_msg,
                    'token':'123456',
                    'user_id':store.state.user_id,
                    'nickname':store.state.nickname,
                    'friend_id':this.friend_id
                }
                var data_index = -1
                for(var i in store.state.all_mag_data) {
                    if(store.state.all_mag_data[i].friend_id == msg_obj.friend_id) {
                        data_index = i
                    }
                }
                if(data_index == -1) {
                    var msg_item = {
                        friend_id: msg_obj.friend_id,
                        nickname: this.nickname,
                        friend_url: '',
                        msg_data: []
                    }
                    msg_item.msg_data.push(msg_obj)
                    store.state.all_mag_data.push(msg_item)
                } else {
                    store.state.all_mag_data[data_index].msg_data.push(msg_obj)
                }
                window.s.send(JSON.stringify(msg_obj))

                // 添加完内容，清空
                this.send_msg = ''
            },
            scrollToBottom() {
                this.$nextTick(() => {
                    var container = this.$el.querySelector("#words");
                    container.scrollTop = container.scrollHeight;
                })
            },
            to_back(){
                // this.$router.go(-1)
                this.$router.push({ name: 'chatview'})
            },
        },
        mounted () {
            this.scrollToBottom();
        },
        updated:function(){
            this.scrollToBottom();
        },
        created: function() {
            console.log(this.$route.params.friend_id)
        }
    }
</script>

<style scoped>
    .icontent{
        width: 100%;
        height: 100%;
    }
    .my-chating-content{
        width: 100%;
        height: calc(100% - 90px);
        overflow: hidden;
        /* background-color: #ef8201; */
    }
    .my-chating-show{
        width:100%;
        height:100%;
        background:#eaeaea;
        margin:0;
        overflow-y: scroll;
    }
    .my-chating-show::-webkit-scrollbar {
        display: none;
    }
    .atalk{
        margin:10px; 
        text-align:left;
        padding-right: 20%;
    }
    .atalk span{
        display:inline-block;
        background:hsl(133, 99%, 40%);
        border-radius:10px;
        color:#000000;
        padding:5px 10px;
    }
    .btalk{
        padding-left: 20%;
        margin:10px;
        text-align:right;
    }
    .btalk span{
        display:inline-block;
        background:white;
        border-radius:10px;
        color:#000000;
        padding:5px 10px;
        text-align:left;
    }
    .my-chat-input{
        overflow: hidden;
        margin: 0;
        padding: 0;
        height: 40px;
        width: 100%;
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
        border: 1px solid #0F996B;
        border-radius: 4px;
    }
    .my-chat-botton{
        float: right;
        text-align: center;
        width: 60px;
        height: 30px;
        font-size: 18px;
        line-height: 30px;
        background-color: #0F996B;
        color: white;
        border-radius: 4px;
        margin: 5px 5px 0 0;
    }
</style>
<template>
    <div>
        <div>
            <mu-appbar style="width: 100%;height: 50px;" color="primary">
                <mu-button icon slot="left">
                    <mu-icon value="menu"></mu-icon>
                </mu-button>
                <mu-button flat slot="right" @click="to_addfriend">
                    <mu-icon size="32" value="add"></mu-icon>
                </mu-button>
            </mu-appbar>
        </div>
        <div id="chat_app">
            <router-view/>
        </div>
        <div class="footer">
            <mu-container>
                <mu-bottom-nav>
                    <mu-bottom-nav-item title="消息" :to="{ name: 'chatview',}" icon="chat"></mu-bottom-nav-item>
                    <mu-bottom-nav-item title="好友" :to="{ name: 'friendsview',}" icon="contacts"></mu-bottom-nav-item>
                    <mu-bottom-nav-item title="我的" :to="{ name: 'userinfoview',}"  icon="account_circle"></mu-bottom-nav-item>
                </mu-bottom-nav>
            </mu-container>
        </div>
    </div>
</template>

<script>
  import $ from 'jquery'
  import { login, getInfo, register, logout, getUserfriends, getFriendInfo, addFriend } from '@/api/chat'
//   var oHeight = $(document).height(); //屏幕当前的高度
//   // alert(oHeight)
//   $(window).resize(function(){
//     // alert('ok')
//     if($(document).height() < oHeight){
//       $(".footer").css("position","static");
//     }else{
//       $(".footer").css("position","fixed");
//     }
//   });
  export default {
    name: "chatbase",
    data () {
      return {
        docked: false,
        open: false,
        position: 'left',
      }
    },
    methods: {
        to_chat() {
            this.$router.push({ name: 'chatview'})
        },
        to_friends() {
            this.$router.push({ name: 'friendsview'})
        },
        to_userinfo() {
            this.$router.push({ name: 'userinfoview'})
        },
        to_addfriend() {
            this.$router.push({ name: 'addfriend'})
        }
    },
    created: function() {
      this.clientHeight = `${document.documentElement.clientHeight}`
    //   alert(this.clientHeight)
    },
    watch:{
      $route(to,from){
        console.log(to.path);
        // switch (to.path) {
        //   case '/home':
        //     break
        //   case '/course':
        //     break
        //   case '/user':
        //     break
        //   case '/login':
        //     console.log(to.path);
        //     break
        //   default:
        //     console.log(to.path);
        //     break
        // }
      }
    },
  }
</script>

<style scoped>
.footer{
    position: fixed;
    left: 0;
    bottom: 0;
    border-top: #eeeeee solid 1px;
    background: #fffffe;
    width: 100%;
}
</style>

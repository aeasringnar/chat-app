var ws = require("nodejs-websocket")
// var http_fuc = require("./axios_fuc")

var AllUserData = new Array()
var HistoryMsg = new Array()
var HistoryAddFriendMsg = new Array()
var server = ws.createServer(function (conn) {
    console.log("新的链接")
    conn.on("text", function (message) {
        console.log("Received:"+message)
        msg_obj = JSON.parse(message)
        switch(msg_obj.msg_type) {
            case 1:
                // console.log(msg_obj)
                var is_friend_online = false
                var friend_index = 0
                for(var i in AllUserData) {
                    if(AllUserData[i].user_id == msg_obj.friend_id) {
                        if(AllUserData[i].user_status == 1) {
                            is_friend_online = true
                            friend_index = i
                        }
                    }
                }
                if(is_friend_online) {
                    console.log('friend_index')
                    console.log(friend_index)
                    AllUserData[friend_index].ws.sendText(JSON.stringify(msg_obj))
                } else {
                    console.log('发现对方不在线，保存为历史消息')
                    msg_obj.msg_status = 1
                    HistoryMsg.push(msg_obj)
                }
                break;
            case 2:
                console.log(msg_obj)
                var is_friend_online = false
                var friend_index = 0
                for(var i in AllUserData) {
                    if(AllUserData[i].user_id == msg_obj.friend_id) {
                        if(AllUserData[i].user_status == 1) {
                            is_friend_online = true
                            friend_index = i
                        }
                    }
                }
                if(is_friend_online) {
                    AllUserData[friend_index].ws.sendText(JSON.stringify(msg_obj))
                } else {
                    console.log('发现对方不在线，保存为历史添加好友消息')
                    msg_obj.msg_status = 1
                    HistoryAddFriendMsg.push(msg_obj)
                }
                break;
            case 3:
                // console.log(msg_obj)
                var is_have_user = false
                var user_index = 0
                // 检查登录的用户在用户表中是否存在
                for(var i in AllUserData) {
                    if(AllUserData[i].user_id == msg_obj.user_id) {
                        is_have_user = true
                        user_index = i
                    }
                }
                // 如果已经存在，那么就是将用户置为在线，并更换ws
                if(is_have_user) {
                    AllUserData[user_index].token = msg_obj.token
                    AllUserData[user_index].user_status = 1
                    AllUserData[user_index].ws = conn
                    console.log('用户重新登录成功')
                    console.log('index:',user_index,'user_id:',msg_obj.user_id)
                    conn.sendText(JSON.stringify({msg:'登录成功'}))
                    // 查询是否存在历史消息，如果存在那么就发送给用户
                    for(var j in HistoryMsg) {
                        if(HistoryMsg[j].friend_id == msg_obj.user_id && HistoryMsg[j].msg_status == 1) {
                            console.log('发现有未读历史消息:')
                            console.log(HistoryMsg[j])
                            AllUserData[user_index].ws.sendText(JSON.stringify(HistoryMsg[j]))
                            HistoryMsg[j].msg_status = 0
                        }
                    }
                    for(var k in HistoryAddFriendMsg) {
                        if(HistoryAddFriendMsg[k].friend_id == msg_obj.user_id && HistoryAddFriendMsg[k].msg_status == 1) {
                            console.log('发现有未读历史添加好友消息:')
                            console.log(HistoryAddFriendMsg[k])
                            AllUserData[user_index].ws.sendText(JSON.stringify(HistoryAddFriendMsg[k]))
                            HistoryAddFriendMsg[k].msg_status = 0
                        }
                    }
                } else {
                    // 不存在时，就添加新的用户到数组中
                    var new_user_obj = {
                        'user_id':msg_obj.user_id,
                        'token':msg_obj.token,
                        'user_status':1,
                        'ws':conn
                    }
                    AllUserData.push(new_user_obj)
                    console.log('新用户登录成功')
                    console.log('index:',(AllUserData.length - 1),'user_id:',msg_obj.user_id)
                    conn.sendText(JSON.stringify({msg:'登录成功'}))
                    for(var j in HistoryMsg) {
                        if(HistoryMsg[j].friend_id == msg_obj.user_id && HistoryMsg[j].msg_status == 1) {
                            console.log('发现有未读历史消息:')
                            console.log(HistoryMsg[j])
                            new_user_obj.ws.sendText(JSON.stringify(HistoryMsg[j]))
                            HistoryMsg[j].msg_status = 0
                        }
                    }
                    for(var k in HistoryAddFriendMsg) {
                        if(HistoryAddFriendMsg[k].friend_id == msg_obj.user_id && HistoryAddFriendMsg[k].msg_status == 1) {
                            console.log('发现有未读历史添加好友消息:')
                            console.log(HistoryAddFriendMsg[k])
                            new_user_obj.ws.sendText(JSON.stringify(HistoryAddFriendMsg[k]))
                            HistoryAddFriendMsg[k].msg_status = 0
                        }
                    }
                }
                break;
            default:
                console.log('未知消息类型...')
                console.log(msg_obj)
        }
    })
    conn.on("close", function (code, reason) {
        console.log("发现有链接关闭")
        for (var i in AllUserData) {
            if (AllUserData[i].ws == conn) {
                // console.log(AllUserData[i])
                AllUserData[i].user_status = 0
            }
        }
    })
}).listen(8801, "0.0.0.0")
console.log("开始监听：ws://0.0.0.0:8801 按 ctrl+c 结束")
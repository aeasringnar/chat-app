# chat-app

#### 介绍
一个基于django、nodejs、vue的websocket实时点对点通讯项目，关键词 QQ、微信、实时聊天、django、vue、nodejs、websocket。

#### 软件架构
本项目完成的功能：注册登录、搜索添加好友、好友之间点对点实时通讯、信息查看、历史消息记录。
项目http服务端又django提供
项目websocket服务端由nodejs提供
项目前端部分由vue提供
项目主要数据库MySQL


#### 安装教程

1. 如何运行django服务端(这里执行的命令需要在chat_app目录下执行):
    建立你的虚拟环境，按照requirements.txt将所有第三方包安装好，
    pip install -r requirements.txt
    我在开发中使用的是MySQL，当然你也可以使用自带的开发数据库db.sqlite3
        无论你选择什么数据库，不要忘记迁移数据
        python manage.py makemigration
        python manage.py migrate
    运行你的django服务
    python manage.py runserver

2. 如何运行nodejs服务端

    提前安装好nodejs的开发环境，在包含文件 websocket_server.js 的目录(websocket_serever)下执行

    npm install nodejs-websocket  

    node websocket_server.js

3. 如何运行vue客户端
    在vue_websocket_chat_app目录下
    npm install (如果你在国内，你可能需要使用cnpm install)
    确保没有报错后
    npm run dev

#### 使用说明

1. 确保你的所有无法都运行正常，如果有报错请先解决，或者联系我。
2. 浏览器访问 http://127.0.0.1:8090/#/login 登录(无账号需要注册,注意这里手机号可以随意输入，例如17312345601等)
3. 开始你的使用

### 相关演示

注册

![image](https://img-blog.csdnimg.cn/20190515134644583.gif)

添加好友

![](https://img-blog.csdnimg.cn/20190515134631939.gif)

登录、聊天、历史消息

![image](https://img-blog.csdnimg.cn/20181221205930919.gif)

#### 参与贡献

1. Fork 本仓库
2. 新建 Feat_xxx 分支
3. 提交代码
4. 新建 Pull Request


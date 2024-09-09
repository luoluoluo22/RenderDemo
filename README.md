# My Flask App

这是一个简单的 Flask 应用程序示例，展示如何使用环境变量和 Docker 部署到 Render.com。

## 步骤
1.登录：https://render.com/

2.选择 Web Service 并连接到你的 Git 仓库

3.配置 Docker 部署：
Build Command：docker build -t flask-app .
Start Command：docker run -p 5000:5000 flask-app
在 Render 的环境变量设置中添加 MESSAGE。

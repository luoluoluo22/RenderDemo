# 使用官方的 Python 基础镜像
FROM python:3.10-slim

# 设置工作目录
WORKDIR /app

# 复制当前目录的内容到工作目录
COPY . .

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 暴露应用端口
EXPOSE 5000

# 设置环境变量以指示 Flask 在生产模式下运行
ENV FLASK_ENV=production

# 启动 Flask 应用
CMD ["python", "app.py"]

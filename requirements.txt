from flask import Flask
import os

app = Flask(__name__)

# 使用环境变量获取消息
message = os.getenv('MESSAGE', 'Hello, World!')

@app.route('/')
def hello():
    return message

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

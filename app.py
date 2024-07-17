from flask import Flask
import os
from dotenv import load_dotenv

# 加载 .env 文件
load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
    db_host = os.getenv('DB_HOST')
    db_user = os.getenv('DB_USER')
    db_pass = os.getenv('DB_PASS')
    db_name = os.getenv('DB_NAME')
    return (f"Database connection details:<br>"
            f"Host: {db_host}<br>"
            f"User: {db_user}<br>"
            f"Password: {db_pass}<br>"
            f"Database Name: {db_name}<br>")

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

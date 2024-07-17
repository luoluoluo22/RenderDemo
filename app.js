// app.js 或 index.js

// 加载 .env 文件
require('dotenv').config();

// 现在可以使用 process.env 来访问环境变量
const dbHost = process.env.DB_HOST;
const dbUser = process.env.DB_USER;
const dbPass = process.env.DB_PASS;
const dbName = process.env.DB_NAME;
const apiKey = process.env.API_KEY;
const port = process.env.PORT || 3000;

console.log(`Connecting to database at ${dbHost} with user ${dbUser}`);
console.log(`Starting server on port ${port}`);

// 假设你使用 Express.js
const express = require('express');
const app = express();

app.listen(port, () => {
    console.log(`Server running on port ${port}`);
});

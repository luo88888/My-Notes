### 模块
* 在微信小程序中，为了提高代码的可复用性，通常会将一些公共的代码抽离成单独的JS文件，作为模块使用，每个JS文件均为一个模块。
* 微信小程序提供了模块化开发的语法，可以使用 module.exports 语法对外暴露接口，然后在需要使用模块的地方通过 require() 函数引入模块。

* 创建模块文件

首先，创建一个JavaScript文件，例如welcome.js。在这个文件中，可以定义一些函数、变量或类，然后使用module.exports来导出它们。
```sql
// welcome.js
function greet(name) {
    return `Hello, ${name}!`;
}

const message = "Welcome to our application!";

module.exports = {
    greet,
    message
};
```
* 使用模块
接下来，你可以在另一个文件中引入并使用这个模块。假设你有一个主文件app.js，你可以这样写：
```js
// app.js
const welcome = require('./utils/welcome.js'); // 相对路径

console.log(welcome.message); // 输出: Welcome to our application!
console.log(welcome.greet('Alice')); // 输出: Hello, Alice!
Page({
    onLoad: function () {
        console.log(welcome.message)
    }
})
```
### HTTP 请求
HTTP 请求可以分为四部分内容：请求的网址（Request URL）、请求方法（Request Method）、请求头（Request Headers）和请求体（Request Body）。

#### 1 请求的网址
请求的网址即 URL，它可以唯一确定请求的资源。

#### 2 请求的方法
常见的请求方法有两种：**GET** 方法和 **POST** 方法。
1. **GET** 方法：请求指定的网页信息，并返回网页内容，提交的数据最多只有 1024 字节。
1. **POST** 方法：向指定资源提交数据并进行请求处理（如提交表单或上传文件），数据都包含在请求体中，提交的数据没有字节限制。

#### 3 请求头
请求头是请求的重要组成部分，在编写爬虫程序时，大部分情况下都需要设置请求头。不同的请求的请求头包含的内容不同。常见的请求头及其说明如下：
请求头|说明
:-:|:-:
Accept|指定客户端可识别的内容类型
Accpet-Encoding|指定客户端可识别的编码
Accpet-Language|指定客户端可识别的语言类型
Cookie|网站为了辨别用户身份进行会话跟踪而存储在用户本地的数据，只要功能是维持当前访问会话
Host|指定请求的服务器域名和端口号
User-Agent|使服务器识别客户端使用的操作系统版本、浏览器及版本等信息，实现爬虫时加上此信息，可以伪装成浏览器
Content-Type|请求的媒体类型信息
Content-Length|请求的内容长度
Referer|包含一个 URL，用户以该 URL 代表的页面出发访问当前请求页面
application/x-www-form-urlencoded|表单数据
multipart/form-data|表单文件
application/json|序列化 JSON 数据
text/xml|XML 数据
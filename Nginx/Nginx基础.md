#### 基本命令

- **启动Nginx**
    ```bash
    cd C:\nginx
    start nginx
    ```

- **​停止Nginx：**
    ```bash
    nginx -s stop   # 快速停止
    nginx -s quit    # 优雅停止
    ```

- **重新加载配置**
    ```bash
    nginx -s reload
    ```

- **​强制终止进程​（若命令失效）：**
    ```bash
    taskkill /f /im nginx.exe
    ```

#### 配置文件
配置文件位于 conf/nginx.conf。用文本编辑器（如VS Code）修改后需重载配置生效。

**常用配置示例**

- **静态网站**
    ```nginx
    server {
        listen       80;
        server_name  localhost;
        location / {
            root   html;       # 网站根目录（默认：nginx目录下的html文件夹）
            index  index.html;
        }
    }
    ```

- **反向代理**
    ```nginx
    server {
        listen 80;
        server_name localhost;
        location / {
            proxy_pass http://localhost:3000;  # 转发到本地3000端口服务
            proxy_set_header Host $host;
        }
    }
    ```

- **检查配置语法**
    ```bash
    nginx -t
    ```
    
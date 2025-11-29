* **将API-Key添加到环境变量**
    * 方式一：添加临时性环境变量
        如果您仅需要在当前会话中添加并使用临时性环境变量，可以运行以下命令：  
        ```
        # 用您的 API Key 代替 YOUR_DASHSCOPE_API_KEY
        set DASHSCOPE_API_KEY="YOUR_DASHSCOPE_API_KEY"
        ```
        您可以在当前会话运行以下命令检查环境变量是否生效：
        `echo %DASHSCOPE_API_KEY%`
    * 方式二：对当前用户添加永久性环境变量
        当您在CMD中需要为当前用户添加永久性环境变量时，可以运行以下命令：
        ```
        # 用您的 API Key 代替 YOUR_DASHSCOPE_API_KEY
        setx DASHSCOPE_API_KEY "YOUR_DASHSCOPE_API_KEY"
        ```
        您可以新建一个会话，运行以下命令检查环境变量是否生效：
        `echo %DASHSCOPE_API_KEY%`
* **获取环境变量中的API-Key**
    `api_key=os.getenv("DASHSCOPE_API_KEY")`
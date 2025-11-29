### 1. 常用命令

1. **查看当前文件夹下的所有文件** `ls` 
1. **克隆文件** `git clone` 
1. **放弃最后一次提交以来的所有改变** `git restore .` 
1. **查看提交历史** `git log` 
1. **查看提交历史** `git log --pretty=oneline` 或 `git log --oneline`
1. **检出以前的提交** `git checkout* 前6个字符`

1. **查看全局配置** `git config --global --list` 
1. **查看系统配置** `git config --system --list` 
1. **查看局部配置** `git config --local --list` 
2. 
1. **与远程仓库关联--------BigBig** `git remote add origin remote_url` 
1. **更新 origin 的 URL** `git remote set-url origin <url>`
2. 
1. **禁用SSL验证（不推荐）** `git config --global http.sslVerify false`
1. **启用SSL验证** `git config --global http.sslVerify true`

### 2. 跟踪文件
1. **停止跟踪*file*及其子文件** `git rm -r --cached file` 
1. **停止跟踪所有文件** `git rm -r --cached .` 
1. **列出跟踪的文件** `git ls-files`

### 查看远程仓库


### 3. 分支
1. **默认分支**
    - 当你初始化一个新的Git仓库时，默认会有一个名为 **master** 或 **main** 的分支。这是项目的主线分支。
    - 这个分支通常用于存放稳定的代码，准备发布的版本等。
1. **创建新的分支** 
    `git branch <branch_name>`
    `git checkout -b <branch_name>` 创建分支并切换到该分支
1. **将本地分支推送到远程仓库**
    推送本地分支 new-branch 到远程仓库 origin，并设置上游跟踪
    `git push -u origin <branch_name>` branch_name是本地分支名称

1. **将本地分支 `server` 推送到远程分支 `remote-server`**
`git push -u origin server:remote-server`


1. **更改分支名称**
    `git branch -m <oldname> <newname>`
1. **切换分支** 
    `git checkout <branch_name>` 或 `git switch <branch_name>`
    `git checkout -b <branch_name>` 分支不存在则会新建
1. **合并分支**
    - 当你在某个分支上完成工作后，可以将这个分支的更改合并回主线分支或其他分支。
    - 合并分支可以使用 `git merge <branch_to_merge> `命令。
1. **删除分支**
    - 如果一个分支已经完成了它的使命，并且其更改已经被合并到了主线分支，你可以安全地删除它。
    - 删除本地分支使用 `git branch -d <branch_name>`，如果要强制删除未合并的分支，可以使用 -D 选项。
    - 删除远程分支可以使用 `git push origin --delete <branch_name>`。
1. **查看分支**
    - 使用 `git branch` 命令可以列出所有本地分支。
    - 使用 `git branch -r` 可以查看所有远程分支。
    - 使用 `git branch -a` 可以同时查看本地和远程的所有分支。
1. **跟踪分支**
    - 一个本地分支可以设置为跟踪一个远程分支。这样当你推送或拉取代码时，Git知道要与哪个远程分支交互。
    - 设置跟踪关系可以使用 `git push --set-upstream origin <branch_name>` 或者在第一次推送时直接指定上游分支

1. **查看追踪关系**
    ```bash
    git branch -vv
    # 输出示例：
    # * new-branch 7d3f21c [origin/new-branch] 添加新功能
    ```

1. **推送你本地的 master 分支到远程仓库 origin 的 master 分支。设置本地的 master 
    分支跟踪远程仓库 origin 的 master 分支。**
    `git push --set-upstream origin master`
1. ** 取消追踪关系** `git branch --unset-upstream`

### 4. .gitignore文件语法
1. 空行会被忽略。
1. 以 # 开头的行是注释行，会被忽略。
1. 通配符：
    * *匹配零个或多个字符。
    * ? 匹配单个字符。
    * [abc] 匹配方括号中的任意一个字符。
1. 路径：
    * 以斜杠（/）开头的模式表示相对于项目根目录的路径。
    * 不以 / 结尾的模式匹配文件和目录（如 build 忽略文件或目录，若为目录则递归忽略内容）。
    * 使用 `**/` 匹配任意层级子目录（如 `**/temp` 忽略所有 temp 目录/文件）。
1. 目录与文件：
    * 以（/）结尾表示**目录**，否则表示**文件**与**目录**。
1. 反斜杠转义：
    * \ 可用于转义特殊字符。
1. 否定模式：
    * 以 ! 开头的模式表示例外规则，即不忽略匹配该模式的文件或目录。
#### 示例
1. 忽略所有 .log 文件
    `*.log`

1. 忽略所有 .tmp 文件，但不忽略 special.tmp
    `*.tmp`
    `!special.tmp`

1. 忽略文件夹 build/
    `build/`

1. 忽略所有 .DS_Store 文件
    `.DS_Store`

1. 只忽略项目目录下的TODO文件，不忽略子目录中的同名文件
    `/TODO`

1. 忽略某一特定文件
    `secret.txt`

1. 忽略某个特定目录及其全部内容
    `mydir/`

1. 忽略 mydir 目录下的所有 .log 文件
    `mydir/*.log`

1. 忽略 mydir 目录及其子目录下的所有 .log 文件：
    `mydir/**/*..log`

### 5. 配置用户信息
* git config --global user.name your_name
* git config --global user.email you_email`


### 6. 推送或拉取失败

#### 检查网络连接，尝试访问 github 官网、ping github.com

---

#### 检查 git 代理配置

* 查看当前代理配置
    ```bash
    git config --global --get http.proxy
    git config --global --get https.proxy
    ```
* 临时关闭 git 代理
    ```bash
    git config --global --unset http.proxy
    git config --global --unset https.proxy
    ```
    
---

#### 切换 SSH 协议（推荐）

生成 SSH 密钥并添加到 GitHub

```BASH
cd ~/.ssh
ls  #看是否存在 id_rsa 和 id_rsa.pub文件，如果存在，说明已经有SSH Key，可以直接用
cat id_rsa.pub  # 查看公钥


ssh-keygen -t ed25519 -C "your_email@example.com"
cat ~/.ssh/id_ed25519.pub
```
将公钥粘贴到 GitHub → Settings → SSH and GPG keys。

修改远程仓库地址为 SSH

```BASH
git remote set-url origin git@github.com:luo88888/wechat-bot.git
```
重新推送

```BASH
git push --set-upstream origin master
```
优势：
SSH 协议比 HTTPS 更稳定，且避免了证书问题。

---

#### 临时关闭 SSL 验证（测试用）
步骤：
```BASH
git config --global http.sslVerify false
```
推送成功后，务必恢复 SSL 验证：

```BASH
git config --global http.sslVerify true
```
警告：
此操作会跳过 SSL 证书检查，仅用于临时测试，长期使用有安全风险。

---

#### 梯子
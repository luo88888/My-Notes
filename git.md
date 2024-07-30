### 命令

1. *ls* 查看当前文件夹下的所有文件
1. *cd* 进入指定的文件夹
1. *git clone* 克隆文件
1. *git restore .* 放弃最后一次提交以来的所有改变
1. *git log* 查看提交历史
1. *git log --pretty=oneline* 查看提交历史
1. *git checkout* 前6个字符，检出以前的提交
1. *git rm -r --cached **file*** 停止跟踪*file*及其子文件
1. *git rm -r --cached .* 停止跟踪所有文件
1. *git ls-files* 列出跟踪的文件
1. *git config --global --list* 查看全局配置
1. *git config --system --list* 查看系统配置
1. *git config --local --list* 查看局部配置
1. *git remote add origin **remote_url*** 与远程仓库关联--------BigBig

### .gitignore文件语法
1. 空行会被忽略。
1. 以 # 开头的行是注释行，会被忽略。
1. 通配符：
    * *匹配零个或多个字符。
    * ? 匹配单个字符。
    * [abc] 匹配方括号中的任意一个字符。
1. 路径：
    * 以斜杠（/）开头的模式表示目录。
    * 如果不以斜杠开头，则匹配文件或目录。
1. 反斜杠转义：
    * \ 可用于转义特殊字符。
1. 否定模式：
    * 以 ! 开头的模式表示例外规则，即不忽略匹配该模式的文件或目录。
#### 实例
##### 忽略所有 .log 文件
*.log

##### 忽略所有 .tmp 文件，但不忽略 special.tmp
*.tmp
!special.tmp

##### 忽略文件夹 build/
build/

##### 忽略所有 .DS_Store 文件
.DS_Store

##### 只忽略项目目录下的TODO文件，不忽略子目录中的同名文件
/TODO

##### 忽略某一特定文件
secret.txt

##### 忽略某个特定目录及其全部内容
mydir/

##### 忽略 mydir 目录下的所有 .log 文件
mydir/*.log

### 配置用户信息
* git config --global user.name your_name
* git config --global user.email you_email
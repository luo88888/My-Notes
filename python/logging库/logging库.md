### 【Python】详解 logging 库

Python 的 `logging` 库是 Python 标准库中用于记录日志的模块，它提供了一种灵活且强大的方式来记录应用程序的日志信息。

#### 1. 基本概念
在使用 logging 库之前，需要了解一些基本概念：

- `Logger`：Logger 对象是应用程序中日志的入口点。每个 Logger 都有一个名称，可以通过名字获取 Logger 实例。

- `Handler`：Handler 负责将日志记录发送到目的地，如控制台、文件等。

- `Formatter`：Formatter 定义了日志记录的输出格式。

- `Filter`：Filter 可以用于过滤日志记录，决定是否处理某条日志。

- `Level`：日志级别，用于表示日志的严重程度，如 DEBUG、INFO、WARNING、ERROR、CRITICAL 等。

2. 基本用法
以下是一个简单的示例，演示如何使用 logging 库记录日志：

```python
import logging

# 配置日志
logging.basicConfig(level=logging.DEBUG, filename='./app.log', filemode='a',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# 创建 Logger
logger = logging.getLogger('example_logger')

# 记录日志
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')
```

### logging.basicConfig：基础设置
```python
import logging

logging.basicConfig(
    level=logging.DEBUG,  # 修改日志级别
    format='%(asctime)s %(name)s [%(pathname)s line:%(lineno)d] %(levelname)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',  # 日期时间格式
    filename='log.txt',  # 日志文件名
    filemode='w'  # 日志模式，如：w：写、a+：追加写 等
)

logging.debug('debug')
logging.info('info')
logging.warning('warning')
logging.error('error')
logging.critical('critical')
```

format 中常用参数：
```python
%(name)s      : logger 的名字
%(asctime)s   : 时间
%(filename)s  : 执行文件名
%(message)s   : 日志信息
%(pathname)s  : 执行程序的路径名
%(process)d   : 进程ID
%(thread)d    : 线程ID
%(threadName)s: 线程名称
%(levelno)s   : 日志级别的数值
%(levelname)s : 日志级别的名称
%(lineno)d    : 调用日志的代码所在行
```

### logging 四个组成部分
英文名|中文名|描述
:-:|:-:|:-:
Logger|记录器|提供程序直接调用的接口，默认名称 root
Handler|处理器|将记录的日志发送到指定位置（终端 or 文件）
Formatter|格式器|用于控制日志信息的输出格式
Filter|过滤器|决定哪些日志被输出

**同时输出到终端和文件**
```python
import logging

# 1.实例化 logger 对象
logger = logging.getLogger('admin')
logger.setLevel(logging.WARNING)  # 设置日志级别

# 2.定义 Handler 对象，常用的有 StreamHandler 和 file_handler
console_handler = logging.StreamHandler()  # 终端
file_handler = logging.FileHandler(filename='log.txt')  # 文件

# 3.定义 Formatter 格式
formatter = logging.Formatter('%(asctime)s %(name)s [%(pathname)s '
                              'line:%(lineno)d] %(levelname)s %(message)s')

# 4.定义 Filter 过滤器：判断给定字符 与 logger 的名称前缀是否匹配
# 可选操作，默认全匹配
# flt = logging.Filter('admin')  # 若匹配则打印

# 5.将 Handler 与 Formatter 绑定、Logger 与 Handler、Filter 绑定
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

# logger.addFilter(flt)

# 6.打印测试
logger.debug('debug')
logger.info('info')
logger.warning('warning')
logger.error('error')
logger.critical('critical')
```
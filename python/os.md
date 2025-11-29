1. **更改工作目录** `os.chdir(path)`
    若目标不存在会抛出 OSError 异常
1. **获取当前工作目录** `os.getcwd()`

#### 获取当前文件所在目录

##### 方法 1：使用 `os.path` 模块（传统方式）
```python
import os

# 获取当前文件的绝对路径（包含文件名）
current_file = os.path.abspath(__file__)
# 提取文件所在目录的路径
current_dir = os.path.dirname(current_file)

print("当前文件目录：", current_dir)
```

说明：

- `__file__` 是 Python 内置变量，表示当前文件的路径（相对或绝对），始终指向当前文件的路径。。
- `os.path.abspath(__file__)` 确保路径是绝对路径。
- `os.path.dirname()` 返回路径的父目录。

##### 方法 2：处理符号链接（推荐）
如果文件是符号链接，建议使用 os.path.realpath 解析真实路径：
```python
import os

# 解析符号链接的真实路径
current_file = os.path.realpath(__file__)
current_dir = os.path.dirname(current_file)

print("真实文件目录：", current_dir)
```

##### 方法 3：使用 pathlib（Python 3.4+ 推荐）
面向对象的路径操作，代码更简洁：
```python
from pathlib import Path

# 获取当前文件的绝对路径（自动解析符号链接）
current_file = Path(__file__).resolve()
# 提取父目录
current_dir = current_file.parent

print("文件目录（pathlib）：", current_dir)
```
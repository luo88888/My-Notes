import logging
import os

# 获取当前文件的绝对路径（包含文件名）
current_file = os.path.abspath(__file__)
# 提取文件所在目录的路径
current_dir = os.path.dirname(current_file)

print("当前文件目录：", current_dir)

# 配置日志
logging.basicConfig(level=logging.DEBUG, filename=current_dir + '/app.log', filemode='a', encoding='utf-8',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# 创建 Logger
logger = logging.getLogger('example_logger')

# 模块A使用独立的 Logger
logger_a = logging.getLogger('module_a')
logger_a.info("模块A日志")

# 模块B使用另一个 Logger
logger_b = logging.getLogger('module_b')
logger_b.error("模块B错误")


# 记录日志
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')

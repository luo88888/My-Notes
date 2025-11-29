import os

# ############################ 获取当前目录 ##############################

# current_directory = os.getcwd()
# print(f'Current directory is: {current_directory}')

# ########################## 获取指定目录下的文件/目录名 ##################

path_directory = './测试'
files = os.listdir(path_directory)
for file in files:
    print(file)

# ############################ 文件重命名 ################################

# path = '.\测试'
# # 获取文件/目录名
# files = os.listdir(path)
# cnt = 1 # 用于构建文件名
# try:
#     for file in files:
#         # 获取文件/目录完整路径
#         full_path = os.path.join(path, file)
#         if os.path.isfile(full_path): # 是文件
#             print(f'{file} 是文件')
#             new_filename = '文件' + str(cnt) + '.txt' # 新文件名
#             cnt += 1
#             # 重命名操作
#             os.rename(full_path, os.path.join(path, new_filename))
#             print(f'File: {file} rename as {new_filename}')
#         else:
#             print(f'{file} 不是文件')
# except OSError as e:
#     print(e)


# ############################## 删除文件 ##################################

# file_path = './测试/文件999.txt'
# if os.path.isfile(file_path):
#     print(f'File: {file_path} exists, proceed to delete.')
#     try:
#         os.remove(file_path)
#         print(f'File: {file_path} deleted successfully.')
#     except OSError as e:
#         print(f'Error occurred: {e}')
# else:
#     print(f'File: {file_path} not exists, skip delete.')

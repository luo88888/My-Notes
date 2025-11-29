# Conda

## 1. 什么是Conda

Conda是一个开源的软件包管理系统和环境管理系统，用于在同一个系统上管理多个Python版本和其依赖项。它类似于pip，但更强大和灵活。

## 2. Conda常用命令

### 2.1 创建环境

```bash
conda create -n myenv python=3.10 [package1[=version]] [package2[=version]] ...
```

参数说明：

- -n: 环境名称（-n 是 --name 的缩写）
- python=3.10: 指定Python版本
- [package1[=version]] [package2[=version]] ...: 指定要安装的包及其版本

### 2.2 克隆环境

```bash
conda create --n new_env --clone old_env
```

参数说明：

- -n: 环境名称
- --clone: 克隆环境
- old_env: 要克隆的环境名称
- new_env: 新环境名称

### 2.3 激活环境

```bash
conda activate myenv
```

### 2.4 退出环境

```bash
conda deactivate
```

### 2.5 删除环境

```bash
conda remove -n myenv --all
```

参数说明：

- -n: 环境名称
- --all: 删除环境及其所有包

### 2.6 查看所有环境

```bash
conda env list
```
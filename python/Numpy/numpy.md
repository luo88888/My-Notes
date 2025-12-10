# NumPy

## 1 简介

NumPy（Numerical Python）是 Python 中用于科学计算的核心库。它提供了高性能的多维数组对象（`ndarray`）以及用于操作这些数组的大量函数。NumPy 是许多其他科学计算库（如 SciPy、Pandas、Matplotlib、Scikit-learn 等）的基础，广泛应用于数据分析、机器学习、图像处理、信号处理等领域。

主要特性包括：

- 高效的 N 维数组对象；
- 广播（Broadcasting）机制，支持不同形状数组间的算术运算；
- 丰富的数学函数（线性代数、傅里叶变换、随机数生成等）；
- 与 C/C++ 和 Fortran 代码集成的能力；
- 内存高效的存储和向量化操作。

## 2 安装

```bash
pip install numpy
```

或使用 Conda：

```bash
conda install numpy
```

导入方式：

```python
import numpy as np
```

> **约定**：通常将 `numpy` 导入为 `np`，这是社区通用惯例。

## 3 常用函数

### 3.1 创建数组

| 函数 | 参数 | 说明 | 示例 |
|:---:|:---:|:---:|:---:|
| `array()` | `obj`: 类数组对象（列表、元组等）<br>`dtype`: 可选数据类型 | 从已有数据创建数组 | `np.array([1, 2, 3])` |
| `zeros()` | `shape`: 整数或整数序列<br>`dtype`: 可选数据类型（默认 `float64`） | 创建全 0 数组 | `np.zeros((3, 3))` |
| `ones()` | `shape`: 整数或整数序列<br>`dtype`: 可选数据类型 | 创建全 1 数组 | `np.ones((2, 4))` |
| `empty()` | `shape`: 整数或整数序列<br>`dtype`: 可选数据类型 | 创建未初始化的“空”数组（含随机值） | `np.empty((2, 2))` |
| `arange()` | `start`: 起始值（可选，默认 0）<br>`stop`: 结束值（不包含）<br>`step`: 步长（可选，默认 1）<br>`dtype`: 可选 | 创建等差一维数组（类似 Python 的 `range`，但返回 `ndarray`） | `np.arange(0, 10, 2)` → `[0, 2, 4, 6, 8]` |
| `linspace()` | `start`: 起始值<br>`stop`: 结束值（**包含**）<br>`num`: 元素个数（默认 50）<br>`endpoint`: 是否包含 `stop`（默认 `True`） | 在指定区间内生成**等间距**的数值 | `np.linspace(0, 10, 5)` → `[0., 2.5, 5., 7.5, 10.]` |
| `logspace()` | `start`: 起始指数（10^start）<br>`stop`: 结束指数（10^stop）<br>`num`: 元素个数<br>`endpoint`: 是否包含 `stop` | 在对数尺度上生成等间距数组 | `np.logspace(0, 2, 3)` → `[1., 10., 100.]` |
| `geomspace()` | `start`: 起始值（必须 > 0）<br>`stop`: 结束值（必须 > 0）<br>`num`: 元素个数 | 生成**几何级数**（等比）数组 | `np.geomspace(1, 1000, 4)` → `[1., 10., 100., 1000.]` |

> ⚠️ 注意：`geomspace` 的 `start` 和 `stop` 是实际数值，不是对数；而 `logspace` 的参数是对数底数（以 10 为底）。

### 3.2 数组属性与基本信息

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])
```

| 属性 | 说明 | 示例 |
|:---:|:---:|:---:|
| `.shape` | 数组维度（元组） | `(2, 3)` |
| `.ndim` | 数组维数 | `2` |
| `.size` | 元素总数 | `6` |
| `.dtype` | 数据类型 | `int64` 或 `float64` 等 |
| `.itemsize` | 每个元素占用的字节数 | `8`（对于 `int64`） |

### 3.3 数组操作

| 函数 | 说明 | 示例 |
|:---:|:---:|:---:|
| `reshape()` | 改变数组形状（不改变数据） | `arr.reshape(3, 2)` |
| `flatten()` / `ravel()` | 展平为一维数组（`flatten` 返回副本，`ravel` 返回视图） | `arr.flatten()` |
| `transpose()` / `.T` | 转置 | `arr.T` |
| `concatenate()` | 沿指定轴连接数组 | `np.concatenate([a, b], axis=0)` |
| `stack()` | 沿新轴堆叠数组 | `np.stack([a, b], axis=0)` |
| `split()` | 分割数组 | `np.split(arr, 2, axis=0)` |

### 3.4 数学运算

| 操作 | 说明 | 示例 |
|:---:|:---:|:---:|
| `+`, `-`, `*`, `/`, `**` | 元素级运算（支持广播） | `a + b` |
| `np.sum()`, `np.mean()`, `np.std()` | 聚合统计 | `np.sum(arr, axis=0)` |
| `np.dot()` / `@` | 矩阵乘法 | `np.dot(A, B)` 或 `A @ B` |
| `np.sqrt()`, `np.exp()`, `np.log()` | 通用数学函数（ufunc） | `np.sqrt(arr)` |

### 3.5 随机数生成（`np.random` 模块）

> 自 NumPy 1.17 起，推荐使用新的随机数生成器 `Generator`。

```python
rng = np.random.default_rng(seed=42)
rng.random((2, 3))        # [0,1) 均匀分布
rng.normal(0, 1, size=5)  # 正态分布
rng.integers(0, 10, size=4)  # 整数随机
```

旧方法（仍可用，但不推荐）：
```python
np.random.rand(2, 3)      # 均匀分布
np.random.randn(2, 3)     # 标准正态分布
np.random.randint(0, 10, size=5)
```

---


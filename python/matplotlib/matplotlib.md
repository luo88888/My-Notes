# Matplotlib

## 1 简介

Matplotlib 是 Python 中最常用的 2D 绘图库之一，广泛用于数据可视化。它提供了类似于 MATLAB 的绘图接口，支持多种输出格式（如 PNG、PDF、SVG 等），并能与 NumPy、Pandas 等科学计算库无缝集成。

常用子模块：

- `matplotlib.pyplot`：类似 MATLAB 的状态机接口（最常用）
- `matplotlib.figure` / `axes`：面向对象接口（更灵活、推荐）

---

## 2 安装与导入

```bash
pip install matplotlib
```

```python
import matplotlib.pyplot as plt
```

常见习惯：

```python
import numpy as np
import matplotlib.pyplot as plt
```

---

## 3 显示中文与负号

Matplotlib 默认不能正确显示中文，正确设置字体后可显示中文：

```python
plt.rcParams["font.sans-serif"] = ["SimHei"]    # 使用电脑自带的字体（黑体）
plt.rcParams["axes.unicode_minus"] = False      # 正确显示负号
```

也可以全局在程序开头设置，例如：

```python
import matplotlib.pyplot as plt

plt.rcParams.update({
    "font.sans-serif": ["SimHei"],
    "axes.unicode_minus": False,
})
```

---

## 4 基本绘图流程（状态机接口 pyplot）

最常见的绘图流程：

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

plt.plot(x, y, label="sin(x)")      # 画线
plt.title("正弦曲线")                # 标题
plt.xlabel("x")                      # x 轴标签
plt.ylabel("y")                      # y 轴标签
plt.legend()                          # 图例
plt.grid(True)                        # 网格
plt.show()                            # 显示
```

关键步骤：
- **准备数据**：`x`, `y`
- **选择绘图函数**：`plot`, `scatter`, `bar`, `hist` 等
- **美化图像**：标题、坐标轴标签、图例、网格
- **显示或保存**：`plt.show()` / `plt.savefig("xxx.png")`

---

## 5 面向对象接口：Figure 与 Axes

更推荐的写法是使用面向对象接口：

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

fig, ax = plt.subplots(figsize=(6, 4))  # 创建画布和坐标轴
ax.plot(x, y, label="sin(x)")
ax.set_title("正弦曲线")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()
ax.grid(True)

plt.show()
```

优点：
- 多子图时更清晰
- 便于对单个坐标轴做精细控制

---

## 6 常见图形

### 6.1 折线图 `plot`

```python
x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]
y2 = [1, 2, 3, 4, 5]

plt.plot(x, y1, color="r", linestyle="-", marker="o", label="平方")
plt.plot(x, y2, color="b", linestyle="--", marker="s", label="一次")
plt.legend()
plt.show()
```

常用参数：

- `color`：`"r"`, `"g"`, `"b"`, `"k"` 或 `"#RRGGBB"`
- `linestyle`：`"-"`, `"--"`, `"-."`, `":"`
- `marker`：点型，如 `"o"`, `"s"`, `"^"` 等

### 6.2 散点图 `scatter`

```python
np.random.seed(0)
x = np.random.randn(100)
y = np.random.randn(100)
colors = np.random.rand(100)
sizes = 50 + 200 * np.random.rand(100)

plt.scatter(x, y, c=colors, s=sizes, alpha=0.6, cmap="viridis")
plt.colorbar(label="颜色值")
plt.title("散点图示例")
plt.show()
```

常用参数：
- `c`：颜色或颜色数组
- `s`：点大小
- `alpha`：透明度
- `cmap`：颜色映射表

### 6.3 柱状图 `bar`

```python
labels = ["A", "B", "C", "D"]
values = [10, 15, 7, 12]

plt.bar(labels, values, color="skyblue")
plt.title("柱状图示例")
plt.xlabel("类别")
plt.ylabel("数值")
plt.show()
```

**并列柱状图**：

```python
import numpy as np

labels = np.array(["A", "B", "C", "D"])
values1 = np.array([10, 15, 7, 12])
values2 = np.array([8, 10, 12, 9])

x = np.arange(len(labels))
width = 0.35

plt.bar(x - width/2, values1, width, label="组1")
plt.bar(x + width/2, values2, width, label="组2")
plt.xticks(x, labels)
plt.legend()
plt.show()
```

### 6.4 直方图 `hist`

```python
np.random.seed(0)
data = np.random.randn(1000)

plt.hist(data, bins=30, color="steelblue", edgecolor="black", alpha=0.7)
plt.title("正态分布直方图")
plt.xlabel("值")
plt.ylabel("频数")
plt.show()
```

常用参数：
- `bins`：柱子数量或分箱边界
- `density=True`：显示概率密度而不是频数

### 6.5 饼图 `pie`

```python
labels = ["A", "B", "C", "D"]
values = [40, 30, 20, 10]
explode = [0.1, 0, 0, 0]  # 突出显示第一个扇区

plt.pie(values, labels=labels, autopct="%1.1f%%", explode=explode,
        shadow=True, startangle=90)
plt.axis("equal")  # 使饼图为正圆
plt.title("饼图示例")
plt.show()
```

### 6.6 箱线图 `boxplot`

```python
np.random.seed(0)
data1 = np.random.randn(100)
data2 = np.random.randn(100) + 2

plt.boxplot([data1, data2], labels=["组1", "组2"])
plt.title("箱线图示例")
plt.show()
```

---

## 7 图形美化与常用设置

### 7.1 标题、坐标轴标签、图例

```python
plt.plot(x, y, label="sin(x)")
plt.title("正弦函数")
plt.xlabel("x 轴")
plt.ylabel("y 轴")
plt.legend(loc="best")  # loc: best, upper right, lower left 等
```

### 7.2 坐标轴范围与刻度

```python
plt.xlim(0, 10)                   # x 轴范围
plt.ylim(-1, 1)                   # y 轴范围
plt.xticks([0, 2, 4, 6, 8, 10])   # 自定义刻度
plt.yticks([-1, 0, 1])
```

也可以对刻度标签进行自定义：

```python
plt.xticks([0, 1, 2, 3], ["一", "二", "三", "四"])
```

### 7.3 网格与注释

```python
plt.grid(True, linestyle="--", alpha=0.5)

# 在图中添加注释
plt.annotate("最大值", xy=(x_max, y_max), xytext=(x_max+0.5, y_max),
             arrowprops=dict(arrowstyle="->", color="red"))
```

### 7.4 线宽、透明度与样式

```python
plt.plot(x, y, color="r", linewidth=2, alpha=0.8, linestyle="--")
```

---

## 8 子图（Subplot）与布局

### 8.1 `plt.subplot`

```python
x = np.linspace(0, 2 * np.pi, 100)

y1 = np.sin(x)
y2 = np.cos(x)

plt.figure(figsize=(8, 4))

plt.subplot(1, 2, 1)  # 1 行 2 列，第一张
plt.plot(x, y1)
plt.title("sin(x)")

plt.subplot(1, 2, 2)  # 1 行 2 列，第二张
plt.plot(x, y2)
plt.title("cos(x)")

plt.tight_layout()
plt.show()
```

### 8.2 `plt.subplots`

```python
fig, axes = plt.subplots(2, 2, figsize=(8, 6))

axes[0, 0].plot(x, np.sin(x))
axes[0, 0].set_title("sin(x)")

axes[0, 1].plot(x, np.cos(x))
axes[0, 1].set_title("cos(x)")

axes[1, 0].plot(x, np.tan(x))
axes[1, 0].set_title("tan(x)")

axes[1, 1].plot(x, np.exp(x/5))
axes[1, 1].set_title("exp(x/5)")

plt.tight_layout()
plt.show()
```

---

## 9 样式与主题

Matplotlib 提供了一些内置样式：

```python
import matplotlib.pyplot as plt
print(plt.style.available)   # 查看可用样式

plt.style.use("ggplot")     # 使用 ggplot 风格
# plt.style.use("seaborn")  # 旧版 seaborn 风格（新版本建议直接使用 seaborn）
```

可以通过 `plt.rcParams` 自定义全局风格，如字体大小、图像尺寸等。

---

## 10 保存图像

```python
plt.plot(x, y)
plt.title("示例")
plt.savefig("example.png", dpi=300, bbox_inches="tight")
plt.show()
```

常用参数：
- `dpi`：分辨率
- `bbox_inches="tight"`：自动裁剪多余空白
- 文件后缀决定格式：`png`, `pdf`, `svg` 等

---

## 11 与 NumPy / Pandas 配合

### 11.1 与 NumPy

上面示例已经大量使用 `numpy` 生成数据，如 `np.linspace`, `np.random.randn` 等。

### 11.2 与 Pandas

Pandas 的 `Series` 和 `DataFrame` 内置了基于 Matplotlib 的绘图接口：

```python
import pandas as pd
import matplotlib.pyplot as plt

s = pd.Series([1, 3, 2, 4])
s.plot(kind="line")
plt.show()
```

DataFrame 也可以直接 `plot`：

```python
df = pd.DataFrame({
    "A": [1, 2, 3, 4],
    "B": [4, 3, 2, 1]
})

ax = df.plot(kind="bar")
ax.set_title("DataFrame 柱状图")
plt.show()
```

---

*最后一次更新：2025-12-07*

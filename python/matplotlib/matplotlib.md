# Matplotlib

## 简介

## 显示中文

Matplotlib 默认不能正确显示中文，正确设置字体后可显示中文
```python
plt.rcParams["font.sans-serif"] = ["SimHei"]    # 使用电脑自带的字体
plt.rcParams["axes.unicode_minus"] = False      # 
```
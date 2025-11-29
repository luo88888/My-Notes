import numpy as np
import matplotlib.pyplot as plt
import os


def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))


# 获取代码文件所在目录
script_dir = os.path.dirname(os.path.abspath(__file__))
# images目录（在代码文件所在目录下）
images_dir = os.path.join(script_dir, "images")

# 创建子图
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# 第一张图：x范围 -5 ~ 5
x1 = np.linspace(-5, 5, 1000)
y1 = sigmoid(x1)
ax1.plot(x1, y1, 'b-', linewidth=2, label='Sigmoid Function')
ax1.grid(True, alpha=0.3)
ax1.set_xlabel('x', fontsize=12)
ax1.set_ylabel('σ(x)', fontsize=12)
ax1.set_title('Sigmoid Function: x ∈ [-5, 5]', fontsize=14)
ax1.axhline(y=0.5, color='r', linestyle='--', alpha=0.7, label='y=0.5')
ax1.axvline(x=0, color='g', linestyle='--', alpha=0.7, label='x=0')
ax1.set_xlim(-5, 5)
ax1.set_ylim(-0.1, 1.1)
ax1.legend(loc='lower right')

# 第二张图：x范围 -50 ~ 50
x2 = np.linspace(-50, 50, 1000)
y2 = sigmoid(x2)
ax2.plot(x2, y2, 'b-', linewidth=2, label='Sigmoid Function')
ax2.grid(True, alpha=0.3)
ax2.set_xlabel('x', fontsize=12)
ax2.set_ylabel('σ(x)', fontsize=12)
ax2.set_title('Sigmoid Function: x ∈ [-50, 50]', fontsize=14)
ax2.axhline(y=0.5, color='r', linestyle='--', alpha=0.7, label='y=0.5')
ax2.axvline(x=0, color='g', linestyle='--', alpha=0.7, label='x=0')
ax2.set_xlim(-50, 50)
ax2.set_ylim(-0.1, 1.1)
ax2.legend(loc='lower right')

# 调整布局
plt.tight_layout()

# 保存图像
os.makedirs(images_dir, exist_ok=True)
output_path = os.path.join(images_dir, "sigma_function_comparison.png")
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"对比图像已保存到: {output_path}")

# 显示图像
plt.show()
"""
    曲线图
    author:Benjamin
"""
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 画布
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(1, 1, 1)

# 数据
x = np.linspace(0, 20, 100000)
y = np.cos(x)
y2 = np.sin(x)

ax.plot(x, y, "red", x, y2, "blue")

# 拉伸和显示
plt.tight_layout()
plt.show()



"""
    折线图，由x和y两个列表分别对应横标和纵标
    author:Benjamin
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 生成两个坐标列表和数据
# 分布中心为100，标准差为20，个数为50
x_data = np.arange(0, 200, 4)
y_data = np.random.normal(100, 20, 50)
x_ticks = np.arange(0, 200, 20)
y_ticks = np.arange(0, y_data.max()+20, 20)

# 窗口和画布
fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot(1, 1, 1)

# 折线图
ax.plot(x_data, y_data, color="k", linewidth=0.5, marker="*", label="百分比")

# 显示图例
ax.legend()

# 横纵坐标的名称
plt.xlabel("数据编号")
plt.ylabel("百分比")

# 拉伸和显示
fig.tight_layout()

plt.show()

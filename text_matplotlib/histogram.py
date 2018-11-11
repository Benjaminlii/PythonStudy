"""
    直方图 可以根据对应区间中元素的个数得到柱的高度
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

np.random.seed(0)

# 分布中心为200 标准差为25 个数为100

x = np.random.normal(200, 25, size=1000)

# 横标和柱的边界(传入数据x 由最大值和最小值以num为步长等分成分区间)
num = 14+1
x_min = x.min()
x_max = x.max()
bins = np.arange(x_min, x_max, (x_max-x_min)/num)

# 建立窗口和尺寸
fig = plt.figure(figsize=(12, 6))
ax1 = fig.add_subplot(1, 1, 1)


# -----------------------------------------------------------------
# bins 指柱形图柱的边缘
# histtype指直方图的类型 bar指并排排列的直方图
#                       barstacked指多个数据堆叠在一起的直方图
#                       step指上轮廓线
#                       stepfilled指填充过的轮廓线
# rwidth指柱形图占的宽度 0~1
# alpha透明度 0~1
# n[0]为统计后各个区间的元素数， n[1]为边界值
# -----------------------------------------------------------------
n = ax1.hist(x, bins, histtype='bar', rwidth=0.9, alpha=1)

# 添加标签
for i in range(len(n[0])):
    plt.text((n[1][i]+n[1][i+1])/2-1, n[0][i]+0.3, "%.0f" % n[0][i])

# 图的名称
ax1.set_title('企业纳税信用得分')

# 设置横坐标为bins 及名称
plt.xticks(bins)
# plt.xlabel('x')
# plt.ylabel('y')

# 纵标
y_ticks = np.arange(0, n[0].max()+20, 20)
plt.yticks(y_ticks)

# 横向参考线
for i in y_ticks:
    plt.plot([x_min, x_max], [i, i], color="black", alpha=0.1)

# 自动调整子图的大小  使之占满整个绘图区域
fig.tight_layout()
plt.show()

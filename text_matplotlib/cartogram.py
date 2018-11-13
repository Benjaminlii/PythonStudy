"""
    三种统计图的封装

    get_histogram(x_data, num)
        参数：data为要进行直方统计的数据组
             num为直方图的区间数
        功能：生成直方图并存入image文件夹
        返回值：void

    get_line_graph(x_data, y_data)
        参数：x_data和y_data分别为折线图各个点坐标的横纵坐标
        功能：生成折线图并保存
        返回值；void

    get_two_line(x_data_0, y_data_0, x_data_1, y_data_1)
        参数：两条线的横纵坐标
        功能：将两条折线图显示在一张图中并保存
        返回值：void

    get_curve()
        未定！！！！！！！！！！！！

    date:2018.11.13
    author:Benjamin
"""

import numpy as np
import matplotlib.pyplot as plt
import sys
import os

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


def get_histogram(data, num):
    # 横标和柱的边界(传入数据x_data,由最大值和最小值以num为步长等分成分区间)
    num += 1
    data_min = data.min()
    data_max = data.max()
    bins = np.arange(data_min, data_max, (data_max - data_min) / num)
    # 建立窗口和尺寸
    fig = plt.figure(figsize=(12, 6))
    ax = fig.add_subplot(1, 1, 1)
    # 画图
    n = ax.hist(data, bins, histtype='bar', rwidth=0.9)
    # 添加标签
    for i in range(len(n[0])):
        plt.text((n[1][i] + n[1][i + 1]) / 2 - 1, n[0][i] + 0.3, "%.0f" % n[0][i])
    # 设置图名称，横纵坐标
    plt.xticks(bins)
    step_size = n[0].max()//10
    step_size -= step_size % 100
    y_ticks = np.arange(0, n[0].max() + step_size, step_size)
    plt.yticks(y_ticks)
    # 横向参考线
    for i in y_ticks:
        plt.plot([data_min, data_max], [i, i], color="black", alpha=0.1)
    # 保存到当前目录下的image文件夹，如果image不存在，创建
    s = str(sys.argv[0]).split("/")
    num = len(s) - 1
    s = "\\".join(s[0:num]) + "\\image"
    if not os.path.exists(s):  # 判断是否存在文件夹
        os.makedirs(s)  # makedirs创建文件时如果路径不存在会创建这个路径
    s = s + "\\histogram"
    plt.savefig(s)

@type(np.ndarray, str, np.ndarray, str, str)
def get_line_graph(x_data, x_name, y_data, y_name, label):
    # 建立窗口和尺寸
    fig = plt.figure(figsize=(12, 6))
    ax = fig.add_subplot(1, 1, 1)
    # 横纵轴
    # ten_x = len(str(x_data.max())) - 2
    # x_step_size = x_data.max() // 10
    # x_step_size -= x_step_size % pow(10, ten_x)
    # print(ten_x)
    # x_ticks = np.arange(0, x_data.max() + x_step_size, x_step_size)
    # ten_x = len(str(y_data.max())) - 2
    # y_step_size = y_data.max() // 10
    # y_step_size -= y_step_size % pow(10, ten_x)
    # y_ticks = np.arange(0, y_data.max() + y_step_size, y_step_size)
    # plt.xticks(x_ticks)
    # plt.yticks(y_ticks)
    # 画图
    ax.plot(x_data, y_data, color="k", linewidth=0.5, marker="*", label=label)
    # 显示图例
    ax.legend()
    # 横纵坐标的名称
    plt.xlabel(x_name)
    plt.ylabel(y_name)
    # 保存到当前目录下的image文件夹，如果image不存在，创建
    s = str(sys.argv[0]).split("/")
    num = len(s) - 1
    s = "\\".join(s[0:num]) + "\\image"
    if not os.path.exists(s):  # 判断是否存在文件夹
        os.makedirs(s)  # makedirs创建文件时如果路径不存在会创建这个路径
    s = s + "\\line_graph"
    plt.savefig(s)


@type(np.ndarray, np.ndarray, str,
      np.ndarray, str,
      str, str)
def get_double_line(x_data, y_data_0, label_0,
                    y_data_1, label_1,
                    x_name, y_name):
    # 建立窗口和尺寸
    fig = plt.figure(figsize=(12, 6))
    ax = fig.add_subplot(1, 1, 1)

    # 画图
    ax.plot(x_data, y_data_0, color="k", linewidth=0.5, marker="*", label=label_0)
    ax.plot(x_data, y_data_1, color="r", linewidth=0.5, marker="*", label=label_1)
    # 显示图例
    ax.legend()
    # 横纵坐标的名称
    plt.xlabel(x_name)
    plt.ylabel(y_name)
    # 保存到当前目录下的image文件夹，如果image不存在，创建
    s = str(sys.argv[0]).split("/")
    num = len(s) - 1
    s = "\\".join(s[0:num]) + "\\image"
    if not os.path.exists(s):  # 判断是否存在文件夹
        os.makedirs(s)  # makedirs创建文件时如果路径不存在会创建这个路径
    s = s + "\\double_line_graph"
    plt.savefig(s)


def get_curve():
    pass

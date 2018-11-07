"""
    测试单选框Radiobutton
    在之前的text里，面向对象效果不好，就面向过程写吧
    author:Benjamin
"""

from tkinter import *

choices = [("Love me", 1),
           ("Marry me", 2),
           ("Destroy me", 3),
           ("Kill me", 4)]

root = Tk()
root.title("Text Radiobutton")
root.geometry("300x150")

frame_chose = LabelFrame(root, text="You have a choice:")
frame_chose.pack(padx=10, pady=10)

# Intvar()返回一个tk变量，表示按钮的状态
v = IntVar()

for choice, num in choices:
    # variable表示当前按钮的状态
    # value表示按钮被点亮时，variable的更新值
    # .pack(anchor= )设置单选项的对齐方式，东南西北等八个方向
    Radiobutton(frame_chose, text=choice, variable=v, value=num).pack(anchor=W)

mainloop()

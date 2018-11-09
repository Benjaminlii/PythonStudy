"""
    练习tkinter中Entry的用法
    author:Benjamin
"""

from tkinter import *

# mark = [["AC", "del", "(", ")"],
#         ["7", "8", "9", "+"],
#         ["4", "5", "6", "-"],
#         ["1", "2", "3", "*"],
#         [".", "0", "=", "/"]]

root = Tk()
root.title("计算器")
# 函数定义----------------------------------------------------


def handle(a):
    if a == "AC":
        v1.set("")
        v2.set("")
        return
    if a == "del":
        s = str(v1.get())
        num = len(s)
        v1.set(str(v1.get())[0:num-1])
        return
    if a == "=":
        try:
            v2.set(eval(v1.get()))
        except SyntaxError:
            v2.set("Error!")
        except ZeroDivisionError:
            v2.set("Error!")
        if v2.get() == "1130" or v2.get() == "520":
            v2.set("I Love You")
        return
    v1.set(v1.get()+str(a))

# 表达式窗口--------------------------------------------------
# 由于计算器的界面安排较为复杂
# 本界面全部用grid排版


expression = Frame(root)\
    .grid(padx=10, pady=10)
# 表达式输入栏
# 可变的输出文本
v1 = StringVar()
# width宽度，font字体大小，state为是否可写（NORMAL可写/DISABLE不可写）
expression_1 = Entry(expression, textvariable=v1, width=20, font=10, state=DISABLED)\
    .grid(row=0, column=0, columnspan=3, padx=10, pady=10)
# 等号
Label(expression, text="=", font=10)\
    .grid(row=0, column=4, padx=0, pady=10)
# 结果
v2 = StringVar()
expression_2 = Entry(expression, textvariable=v2, width=10, font=10, state=DISABLED)\
    .grid(row=0, column=6, padx=10, pady=10)

# 输入按钮窗口------------------------------------------------
input_button = Frame(root)\
    .grid(row=1, column=0, padx=10, pady=10)

# 在Button中command传参中发现如果用循环建立Button会造成传参错误
# 还没有想到解决方法

# for row in range(5):
#     for col in range(4):
#         text = mark[row][col]
#         print("text = %s" % text)
#         fg_ = "red" if(row == 0 and col == 0) else "black"
#         bg_ = "red" if (row == 4 and col == 2) else "white"
#         if row == 4 and col == 2:
#             fg_ = "white"
#         Button(input_button, text=text,
#                fg=fg_, bg=bg_,
#                font=10,
#                width=10, height=2,
#                command=lambda: handle(a=text)) \
#             .grid(row=row+1, column=col*2, padx=5, pady=5)

# 无奈 -_-#
# lambda表达式帮助command传参数
# width和height分别为按钮的宽和高
Button(input_button, text="AC", fg="red", bg="white", font=10, width=10, height=2, command=lambda: handle(a="AC")) \
             .grid(row=1, column=0, padx=5, pady=5)

Button(input_button, text="del", fg="black", bg="white", font=10, width=10, height=2, command=lambda: handle(a="del")) \
             .grid(row=1, column=2, padx=5, pady=5)

Button(input_button, text="(", fg="black", bg="white", font=10, width=10, height=2, command=lambda: handle(a="(")) \
             .grid(row=1, column=4, padx=5, pady=5)

Button(input_button, text=")", fg="black", bg="white", font=10, width=10, height=2, command=lambda: handle(a=")")) \
             .grid(row=1, column=6, padx=5, pady=5)

Button(input_button, text="7", fg="black", bg="white", font=10, width=10, height=2, command=lambda: handle(a="7")) \
             .grid(row=2, column=0, padx=5, pady=5)

Button(input_button, text="8", fg="black", bg="white", font=10, width=10, height=2, command=lambda: handle(a="8")) \
             .grid(row=2, column=2, padx=5, pady=5)

Button(input_button, text="9", fg="black", bg="white", font=10, width=10, height=2, command=lambda: handle(a="9")) \
             .grid(row=2, column=4, padx=5, pady=5)

Button(input_button, text="+", fg="black", bg="white", font=10, width=10, height=2, command=lambda: handle(a="+")) \
             .grid(row=2, column=6, padx=5, pady=5)

Button(input_button, text="4", fg="black", bg="white", font=10, width=10, height=2, command=lambda: handle(a="4")) \
             .grid(row=3, column=0, padx=5, pady=5)

Button(input_button, text="5", fg="black", bg="white", font=10, width=10, height=2, command=lambda: handle(a="5")) \
             .grid(row=3, column=2, padx=5, pady=5)

Button(input_button, text="6", fg="black", bg="white", font=10, width=10, height=2, command=lambda: handle(a="6")) \
             .grid(row=3, column=4, padx=5, pady=5)

Button(input_button, text="-", fg="black", bg="white", font=10, width=10, height=2, command=lambda: handle(a="-")) \
             .grid(row=3, column=6, padx=5, pady=5)

Button(input_button, text="1", fg="black", bg="white", font=10, width=10, height=2, command=lambda: handle(a="1")) \
             .grid(row=4, column=0, padx=5, pady=5)

Button(input_button, text="2", fg="black", bg="white", font=10, width=10, height=2, command=lambda: handle(a="2")) \
             .grid(row=4, column=2, padx=5, pady=5)

Button(input_button, text="3", fg="black", bg="white", font=10, width=10, height=2, command=lambda: handle(a="3")) \
             .grid(row=4, column=4, padx=5, pady=5)

Button(input_button, text="*", fg="black", bg="white", font=10, width=10, height=2, command=lambda: handle(a="*")) \
             .grid(row=4, column=6, padx=5, pady=5)

Button(input_button, text=".", fg="black", bg="white", font=10, width=10, height=2, command=lambda: handle(a=".")) \
             .grid(row=5, column=0, padx=5, pady=5)

Button(input_button, text="0", fg="black", bg="white", font=10, width=10, height=2, command=lambda: handle(a="0")) \
             .grid(row=5, column=2, padx=5, pady=5)

Button(input_button, text="=", fg="white", bg="red", font=10, width=10, height=2, command=lambda: handle(a="=")) \
             .grid(row=5, column=4, padx=5, pady=5)

Button(input_button, text="/", fg="black", bg="white", font=10, width=10, height=2, command=lambda: handle(a="/")) \
             .grid(row=5, column=6, padx=5, pady=5)

# 启动主循环
mainloop()

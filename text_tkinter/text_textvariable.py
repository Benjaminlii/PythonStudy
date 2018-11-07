"""
    用于测试textvariable的用法
    author:Benjamin
"""
from tkinter import *


class App:
    def __init__(self):
        self.root = Tk()
        self.root.title("text variable")
        self.root.geometry("256x128")

        hi_button = Button(self.root, text="say hi", command=self.say_hi)
        hi_button.pack(side="bottom", padx=10, pady=10)

        self.num = 0
        self.var = StringVar()
        self.var.set("hi x %d" % self.num)

        self.hixnum = Label(self.root, textvariable=self.var)
        self.hixnum.pack(side="top", padx=10, pady=10)

    def say_hi(self):
        self.num += 1
        self.var.set("hi x %d" % self.num)


app = App()
mainloop()

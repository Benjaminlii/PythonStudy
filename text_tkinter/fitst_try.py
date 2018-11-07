"""
    之前写了一个tkinter的练习代码
    给弄不见了
    补上一个
    author:Benjamin
"""
from tkinter import *


class App:
    def __init__(self):
        self.root = Tk()
        self.root.title("a title")
        self.root.geometry("256x128")

        self.frame = Frame(self.root)
        self.frame.pack(side=LEFT, padx=10, pady=10)

        self.hi = Button(self.frame, text="say hi", bg="white", fg="black", command=App.say_hi)
        self.hi.pack()

    @staticmethod
    def say_hi():
        root1 = Tk()
        root1.title("say hi")
        root1.geometry("256x128")
        frame = Frame(root1)
        frame.pack()
        Label(frame, text="hi").pack()


app = App()
mainloop()



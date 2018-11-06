"""
    之前写了一个tkinter的练习代码
    给弄不见了
    补上一个
    author:Benjamin
"""
from tkinter import *


class App:
    def __init__(self, root):
        frame = Frame(root)
        frame.pack()

        self.hi = Button(frame, text="say hi", bg="white", fg="black", command=App.say_hi)
        self.hi.pack()

    @staticmethod
    def say_hi():
        root1 = Tk()
        root1.title("say hi")
        root1.geometry("256x128")
        frame = Frame(root1)
        frame.pack()
        Label(frame, text="hi").pack()


root = Tk()
root.title("a title")
root.geometry("256x128")


app = App(root)
mainloop()



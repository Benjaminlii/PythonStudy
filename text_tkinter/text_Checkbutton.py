"""
    测试复选框Checkbutton的用法
    author:Benjamin
"""

from tkinter import *

choices = ["apple",
           "banana",
           "orange",
           "watermelon"]
v = []

root = Tk()
root.title("Text Checkbutton")
root.geometry("300x150")

frame_choice = LabelFrame(root, text="You can get some fruits:")
frame_choice.pack(padx=10, pady=10)

for choice in choices:
    v.append(vars())
    Checkbutton(frame_choice, text=choice, variable=v[-1]).pack(anchor=W)

mainloop()

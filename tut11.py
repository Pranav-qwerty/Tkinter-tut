from tkinter import *
import tkinter.messagebox as tmg

root = Tk()


def func():
    print("Hello")


def helps():
    tmg.showinfo("Help", 'Pranav will help you')


def rate_us():
    tmg.askquestion("Rate us", "Was your experience good?")


root.geometry('733x566')
# Making a non dropdown menu bar
# menu = Menu(root)
# menu.add_command(label="File", command=func)
# menu.add_command(label="Exit", command=quit)
# root.config(menu=mymenu)

# Making a dropdown menu
menubar = Menu(root)
m1 = Menu(menubar, tearoff=0)
m1.add_command(label="Save", command=func)
m1.add_command(label="Save As", command=func)
m1.add_separator()
m1.add_command(label="Print", command=func)
m1.add_command(label="New", command=func)
root.config(menu=menubar)
menubar.add_cascade(label='File', menu=m1)

m2 = Menu(menubar, tearoff=0)
m2.add_command(label="Save", command=func)
m2.add_command(label="Save As", command=func)
m2.add_separator()
m2.add_command(label="Help", command=helps)
m2.add_command(label="Rate Us", command=rate_us)
root.config(menu=menubar)
menubar.add_cascade(label='Edit', menu=m2)

root.mainloop()

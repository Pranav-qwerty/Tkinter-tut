# Exercise - Make the pycharm welcome screen
from tkinter import *

root = Tk()
root.geometry('733x433')
root.maxsize(733, 433)
root.minsize(733, 433)
label1 = Label(text='PyCharm Community Edition')
label1.pack()

root.mainloop()

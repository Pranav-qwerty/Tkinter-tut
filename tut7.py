from tkinter import *


def getvals():
    print(username.get())
    print(password.get())


root = Tk()
root.geometry('655x555')

a = Label(root, text='User name')
p = Label(root, text='Password')
a.grid(row=1)
p.grid(row=2)

username = StringVar()
password = StringVar()

user_entry = Entry(root, textvariable=username)
password_entry = Entry(root, textvariable=password)

user_entry.grid(row=1, column=2)
password_entry.grid(row=2, column=2)

Button(text="Submit", command=getvals).grid()

root.mainloop()

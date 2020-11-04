# Sublime Text editor

from tkinter import *

root = Tk()

root.geometry('1000x600')

root.title("Sublime Text")

f3 = Frame(root, borderwidth=25, bg='green', relief=SUNKEN)
f3.pack(side=BOTTOM, fill=X)

f1 = Frame(root, bg='blue', borderwidth=6, relief=SUNKEN)
f1.pack(side=LEFT, fill='y')

f2 = Frame(root, borderwidth=8, bg='red', relief=SUNKEN)
f2.pack(side=TOP, fill=X)

f4 = Frame(root, borderwidth=8)
f4.pack(side=BOTTOM)

photo = PhotoImage(file='image.png')
photo_label = Label(f4, image=photo)
photo_label.pack(fill=X)

l2 = Label(f3, text="This is Terminal or Command Prompt", bg='green', fg='white')
l2.pack(padx=300, fill=X)

l1 = Label(f2, text="Welcome To Sublime Text!", bg='red', fg='white', font='comicsans-bold 7 bold')
l1.pack(pady=25, fill=X)

l0 = Label(f1, text='TUTORIAL5 - Sublime Text', bg='blue', fg='white')
l0.pack(pady=200, fill=X)

root.mainloop()

from tkinter import *

root = Tk()
root.geometry('580x500')


def getimg():
    photo = PhotoImage(file='image.png')
    photo_label = Label(image=photo)
    photo_label.pack(anchor='nw')
    root.mainloop()


def Press():
    print("Hello, world!")


# Buttons in tkinter Window

b5 = Button(fg='red', text="Press", bg='green')
b5.pack(side=BOTTOM, anchor='sw')

b4 = Button(fg='red', text="Press", bg='green')
b4.pack(side=BOTTOM, anchor='sw')

b3 = Button(fg='red', text="Press", bg='green')
b3.pack(side=BOTTOM, anchor='sw')


b2 = Button(fg='red', text="Press", bg='green', command=Press)
b2.pack(side=BOTTOM, anchor='sw')

b1 = Button(fg='red', text="Press", bg='green', command=getimg)
b1.pack(side=BOTTOM, anchor='sw')

root.mainloop()

from tkinter import *

root = Tk()


def func(widget):
    print(myslider.get())
    print(myslider2.get())


root.geometry('455x233')
root.title('Tutorial12')
myslider = Scale(root, from_=1, to=255, command=func,
                 tickinterval=50, fg='white')
myslider2 = Scale(root, from_=1, to=255, orient=HORIZONTAL,
                  bg='Green', fg='Red', command=func)
myslider.pack()
myslider2.pack()
root.mainloop()

from tkinter import *

root = Tk()
root.geometry('455x233')


def upload():
    status_var.set("Busy")
    s_ber.update()
    import time
    time.sleep(2)
    status_var.set("Ready")
    s_ber.update()


status_var = StringVar()
status_var.set("Ready")
s_ber = Label(root, textvariable=status_var, relief=SUNKEN, anchor='w', bg="gray", fg="White")
s_ber.pack(side=BOTTOM, fill=X)
Button(root, text="Upload", command=upload).pack()

root.mainloop()

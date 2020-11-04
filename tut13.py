from tkinter import *
import tkinter.messagebox as tmg

root = Tk()
root.geometry("455x233")
root.title("Tutorial13")


def order_now():
    tmg.showinfo("Order Received", f"You will be getting {var.get()} in few minutes")


var = StringVar()
var.set("Nothing")

Label(root, text="What would you like to have sir?", font="lucida 19 bold", justify=LEFT, padx=14).pack()
radio = Radiobutton(root, text="Dosa", padx=14, variable=var, value="Dosa").pack(anchor='w')
radio2 = Radiobutton(root, text="Idli", padx=14, variable=var, value="Idli").pack(anchor='w')
radio3 = Radiobutton(root, text="Samosa", padx=14, variable=var, value="Samosa").pack(anchor='w')
Button(text="Order Now", command=order_now).pack(anchor='w')

root.mainloop()

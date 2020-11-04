from tkinter import *

root = Tk()
root.geometry("455x233")
root.title("Tutorial15")

scrollbar = Scrollbar(root)
scrollbar.pack(fill=Y, side=RIGHT)

lbx = Listbox(root, yscrollcommand=scrollbar.set, bg="Green", fg="Black")
for i in range(344):
    lbx.insert(END, f"Item {i}")
lbx.pack(fill='both', padx=22)
scrollbar.config(command=lbx.yview)
root.mainloop()

from tkinter import *

root = Tk()
root.title('Exercise2')
root.geometry('600x520')
root.minsize(600, 520)
root.maxsize(600, 520)
with open('exercise1.txt', 'r') as f:
    img = PhotoImage(file="1-tree-png-image-download-picture_400x400.png")
    image = Label(image=img)
    image.pack(padx=10, pady=10)
    txt = Label(text=f.read())
    txt.pack(padx=5, pady=5,)
root.mainloop()

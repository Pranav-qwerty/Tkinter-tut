from tkinter import *

root = Tk()


def wer(event):
    print(f"Clicked {event.x}, {event.y}")


root.title("Tutorial9")
root.geometry("644x334")
widget = Button(root, text="Click")
widget.pack()
# getting events of widget
widget.bind('<Button-1>', wer)
widget.bind('<Double-1>', quit)
root.mainloop()

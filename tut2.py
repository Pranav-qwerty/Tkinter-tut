from tkinter import *

root = Tk()
# geometry sets the first appearance of the window
root.geometry('200x100')  # First one is for the width and second for height

# minsize sets the minimum size of the window
root.minsize(200, 100)  # First one is for the width and second for height

# maxsize sets the maximum size of the window
root.maxsize(1200, 800)  # First one is for the width and second for height

# Label
label1 = Label(text="Hello, this the third tutorial!")
# Packing label1
label1.pack()

root.mainloop()

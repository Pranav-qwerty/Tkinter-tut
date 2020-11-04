# Usage of canvas
from tkinter import *

root = Tk()
canvas_width = 800
canvas_height = 400
root.title("Tutorial8")
root.geometry(f"{canvas_width}x{canvas_height}")
can_widget = Canvas(root, width=canvas_width, height=canvas_height)
can_widget.pack()
# The line goes from the point x1, y1, to x2, y2
can_widget.create_line(0, 0, 800, 400, fill='red')
can_widget.create_line(0, 400, 800, 0, fill='red')
# The Rectangle uses arguments Top-Left, and Bottom-Right
can_widget.create_rectangle(300, 100, 700, 300, fill='green')
# Creating text
can_widget.create_text(200, 200, text="Python")
# Creating oval to create a circle take the coordinates of square
can_widget.create_oval(100, 200, 150, 140)
can_widget.create_oval(100, 300, 200, 200, fill="blue")
root.mainloop()

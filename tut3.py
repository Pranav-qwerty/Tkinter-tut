from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry('590x453')
root.minsize(590, 453)
root.maxsize(590, 453)
# Opening op the jpg file
'''
Iage = Image.open('1.jpg')
photo = ImageTk.PhotoImage(Iage)
'''
# Add image to the window
photo = PhotoImage(file='image.png')
# Making the the label of photo
photo_label = Label(image=photo)
# Packing the photo Label
photo_label.pack()
root.mainloop()

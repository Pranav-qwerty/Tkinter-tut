from tkinter import *

root = Tk()
root.geometry('444x333')
root.title('Tutorial 4')

# Important label options
# bd - background
# text - adds the text
# fg - foreground
# font - sets the font
# padx - x padding
# pady - y padding
# relief - border styleing - SUNKEN, RAISED, GROOVE, RIDGE
title_label = Label(text="""Nature, in the broadest sense, is the natural, physical, or material world or universe. 
"Nature" can refer to the phenomena of the physical world, and also to life in general. The study of nature is a 
large, if not the only, part of science. Although humans are part of nature, human activity is often understood as a 
separate category from other natural phenomena.""",
                    bg="black", fg='white', padx=23, pady=44, font='comicsans-bold 7 bold', borderwidth=3,
                    relief=SUNKEN)

# important pack attributes
# anchor = nw, ne, se, sw
# side = top, bottom, left, right - Default = top
# fill = X
# pady
# padx

title_label.pack(side=TOP, fill=X, padx=12, pady=15)
root.mainloop()

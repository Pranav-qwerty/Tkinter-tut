from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

root = Tk()
root.title("Untitled - Notepad")
root.geometry("600x400")
root.minsize(200, 100)
root.iconbitmap("note.ico")


def quity():
    root.destroy()


def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)
    pass


def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt",
                                 filetypes=[("All Files", "*.*"),
                                            ("Text Documents", "*.txt")])
        if file == "":
            file = None
        else:
            f = open(file, 'w')
            f.write(TextArea.get(1.0, END))
            f.close()
            root.title(os.path.basename(file) + " - Notepad")
            print("File saved")
    else:
        f = open(file, 'w')
        f.write(TextArea.get(1.0, END))
        f.close()
        showinfo("Saved", f"Your file has been saved to {file} directory")


def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                      ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()


def cut():
    # noinspection PyRedundantParentheses
    TextArea.event_generate(("<<Cut>>"))


def copy():
    # noinspection PyRedundantParentheses
    TextArea.event_generate(("<<Copy>>"))


def paste():
    # noinspection PyRedundantParentheses
    TextArea.event_generate(("<<Paste>>"))


def he_lp():
    showinfo("Help", """To know more about this Notepad
                Ask from Ax-54""")


def rate_us():
    showinfo("Rate", """If you are satisfied with this notepad
            Please tell to Ax-54
    Else Please suggest to Ax-54

    We will be thankful to you""")


def about():
    showinfo("Info", """This notepad is made by
          Pranav Tripathi
  on Tuesday, 3 November 2020""")


# Text area
TextArea = Text(root, font="lucida 13")
TextArea.pack(fill=BOTH, expand=True)

file = None

# Menu bar
Menubar = Menu(root)
FileMenu = Menu(Menubar, tearoff=0)

FileMenu.add_command(label="New", command=newFile)
FileMenu.add_command(label="Open", command=openFile)
FileMenu.add_command(label="Save", command=saveFile)
FileMenu.add_separator()
FileMenu.add_command(label="Exit", command=quity)

Menubar.add_cascade(label="File", menu=FileMenu)

EditMenu = Menu(Menubar, tearoff=0)

EditMenu.add_command(label="Cut", command=cut)
EditMenu.add_command(label="Copy", command=copy)
EditMenu.add_command(label="Paste", command=paste)
Menubar.add_cascade(label="Edit", menu=EditMenu)

HelpMenu = Menu(Menubar, tearoff=0)

HelpMenu.add_command(label="Help", command=he_lp)
HelpMenu.add_command(label="Rate Us", command=rate_us)
HelpMenu.add_command(label="About Notepad", command=about)
Menubar.add_cascade(label="Extra", menu=HelpMenu)

root.config(menu=Menubar)

Scroll = Scrollbar(TextArea)
Scroll.pack(side=RIGHT, fill=Y)
Scroll.config(command=TextArea.yview)
TextArea.config(yscrollcommand=Scroll.set)

root.mainloop()

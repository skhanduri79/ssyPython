import os
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename


def newFile():
    global file
    root.title("Untitled Notepad")
    file = None
    TextArea.delete((1.0, END))


def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents","*.txt")
                                      ])

    if file=="":
        file=None

    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file,"r")
        TextArea.insert(1.0,f.read())
        f.close()

def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt",
                               filetypes=[("All Files", "*.*"),
                                     ("Text Documents","*.txt")])
        if file=="":
            file=None
        else:
            # save as a new file
            f = open(file,"w")
            f.write(TextArea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file)+" - Notepad")
            print("file saved")
    else:
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()
        root.title(os.path.basename(file) + " - Notepad")
        print("file saved")



def exitFile():
    root.destroy()


def cutFile():
    TextArea.event_generate("<<Cut>>")


def copyFile():
    TextArea.event_generate("<<Copy>>")


def pasteFile():
    TextArea.event_generate("<<Paste>>")


def aboutApp():
    showinfo("Notepad", "Notepad by Sakshi")
# this is an trial comment


if __name__ == "__main__":
    # basic setup
    root = Tk()
    root.title("Untitled-Notepad")
    root.geometry("644x780")

    # Adding text area
    TextArea = Text(root, font="lucid 13")
    file = None
    TextArea.pack(fill=BOTH, expand=True)

    # Menu bar
    MenuBar = Menu(root)
    FileMenu = Menu(MenuBar, tearoff=0)

    # to open a new file
    FileMenu.add_command(label="New", command=newFile)

    # to open a already existing file
    FileMenu.add_command(label="Open", command=openFile)

    # to save a current file
    FileMenu.add_command(label="Save", command=saveFile)

    FileMenu.add_separator()

    # to exit
    FileMenu.add_command(label="Exit", command=exitFile)
    MenuBar.add_cascade(label="File", menu=FileMenu)

    # edit menu starts
    EditMenu = Menu(MenuBar, tearoff=0)

    # to give the feature of edit
    EditMenu.add_command(label="Cut", command=cutFile)

    # to give the feature of copy
    EditMenu.add_command(label="Copy", command=copyFile)

    # to give the feature of paste
    EditMenu.add_command(label="Paste", command=pasteFile)
    # EditMenu.add_cascade(label="Edit", menu=EditMenu)
    MenuBar.add_cascade(label="Edit", menu=EditMenu)

    # edit menu ends

    # help menu starts

    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label="About", command=aboutApp)
    MenuBar.add_cascade(label="Help", menu=HelpMenu)

    # help menu ends

    # file menu ends

    root.config(menu=MenuBar)

    # adding scrollbar

    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT, fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)

    root.mainloop()

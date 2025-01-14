from tkinter import *

root = Tk()
root.geometry("644x344")
root.title("Vs Code")

def myfunc():
    print("Hogaya")

# mainmenu = Menu(root)
# mainmenu.add_command(label="File",command=myfunc)
# mainmenu.add_command(label="Exit",command=quit)
# root.config(menu=mainmenu)

mainmenu = Menu(root)
m1 = Menu(mainmenu,tearoff=0)
m1.add_command(label="New Text File",command=myfunc)
m1.add_command(label="New File",command=myfunc)
m1.add_command(label="New Window",command=myfunc)
m1.add_separator()
m1.add_command(label="Open File",command=myfunc)
m1.add_command(label="Open Folder",command=myfunc)
m1.add_separator()
m1.add_command(label="Save",command=myfunc)
m1.add_command(label="Save As",command=myfunc)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="File",menu=m1)

m2 = Menu(mainmenu,tearoff=0)
m2.add_command(label="Undo",command=myfunc)
m2.add_command(label="Redo",command=myfunc)
m2.add_separator()
m2.add_command(label="Cut",command=myfunc)
m2.add_command(label="Copy",command=myfunc)
m2.add_command(label="Paste",command=myfunc)
m2.add_separator()
m2.add_command(label="Find",command=myfunc)
m2.add_command(label="Replace with",command=myfunc)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Edit",menu=m2)

m3 = Menu(mainmenu,tearoff=0)
m3.add_command(label="Exit", command=quit)
m3.add_command(label="Help", command=myfunc)
m3.add_command(label="About us", command=myfunc)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Help",menu=m3)

root.mainloop()
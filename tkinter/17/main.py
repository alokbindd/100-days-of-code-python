from tkinter import *

def add():
    global i
    lbx.insert(ACTIVE,f"{i}")
    i+=1

i = 0
root = Tk()
root.geometry("644x344")
root.title("list box")

lbx =  Listbox(root)
lbx.pack()

lbx.insert(END,"First Item of ListBox")
Button(root,text="Add Item",command=add).pack()

root.mainloop()
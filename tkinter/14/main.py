from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("644x344")
root.title("Vs Code")

def myfunc():
    print("Hogaya")

def help():
    print("Mein karunga apki help")
    tmsg.showinfo("Help kartha hu","Mein karunga apki help")

def Rate():
    value = tmsg.askquestion("Rate us","was your experience god?....using this Gui?")
    print(value)
    if value == "yes":
       msg = "Thanks for Rating, Rate us on appstore"
    else:
        msg = "Thanks for Rating, What went Wrong?"
    tmsg.showinfo("Rating",msg)

def befriendAlice():
    ans = tmsg.askretrycancel("Wanna be friend of Alice","She will not become your friend")
    if ans:
        tmsg.showinfo("friend","Also after retry she will not become your friend")
    else:
        tmsg.showinfo("nice","Good Nice Choice")

def func1():
    ans = tmsg.askyesnocancel("let see","Do You Want to Proceed?")
    print(ans)
    if ans == True:
        print("Good")

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
m3.add_command(label="Help", command=help)
m3.add_command(label="Rate us", command=Rate)
m3.add_command(label="Alice", command=befriendAlice)
m3.add_command(label="trying", command=func1)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Help",menu=m3)



root.mainloop()
# Packing Buttons In Tkinter
from tkinter import *

root = Tk()
root.geometry("800x800")

def Hello():
    print("Hello good Morning")

def bhai1():
    print("Bol Bhai kaise hai?")

def bhai2():
    print("Mast hu bhai tu kaise hai?")

font ="roboto 18 bold"
f1 = Frame(root, borderwidth=6, bg="Black", relief=RIDGE)
Label(f1, text="CLICK ME", font=font, bg="Black", fg="Pink").pack(padx=10, pady=10)
b1 = Button(f1, text="Hello", bg="Grey", fg="Red",font=font, command=Hello).pack(side=LEFT,padx=10, pady=10)
b2 = Button(f1, text="Bro1",bg="Grey", fg="Green",font=font, command=bhai1).pack(side=LEFT,padx=10, pady=10)
b3 = Button(f1, text="Bro2",bg="Grey", fg="Blue",font=font, command=bhai2).pack(side=LEFT,padx=10, pady=10)
f1.pack(side=LEFT,anchor="nw",padx=10, pady=10)

root.mainloop()
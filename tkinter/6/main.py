from tkinter import *

root = Tk()
root.geometry("900x700")

f0 = Frame(root, background="Red" , borderwidth=6, padx= 30, relief=SUNKEN)
Label(f0, text="sidebar" ,font="arial 18 bold").pack()
f0.pack(side=LEFT, fill="y")

f1 = Frame(root, background="Green" , borderwidth=6, padx= 30 , relief= SUNKEN)
Label(f1, text="Menu Bar" ,font="arial 18 bold").pack()
f1.pack(side=TOP, fill="x")

f2 = Frame(root, background="Blue" , borderwidth=6, padx= 30 , relief= SUNKEN)
Label(f2, text="Status Bar" ,font="arial 18 bold").pack()
f2.pack(side=BOTTOM, fill="x")

root.mainloop()
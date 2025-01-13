# Python GUI Exercise 2: Window Resizer GUI 
from tkinter import *

def changeZ():
    w = width_value.get()
    h = Height_value.get()
    root.geometry(f"{w}x{h}")

root = Tk()
root.geometry("344x344")
root.title("Window resizer")
f="Roboto 12"
Label(root,text="Window Resizer",font="Roboto 18 bold",pady=10).grid(row=0,column=1)
Width = Label(root,text="Enter Width",font=f).grid(row=1,column=0,padx=5,pady=5)
Height = Label(root,text="Enter Height",font=f).grid(row=2,column=0,padx=5,pady=5)

width_value = StringVar()
Height_value = StringVar()

Width_entry = Entry(root,textvariable=width_value).grid(row=1,column=1,padx=5,pady=5)
Height_entry = Entry(root,textvariable=Height_value).grid(row=2,column=1,padx=5,pady=5)

Button(root,text="Apply",command=changeZ,font=f).grid(row=3,column=1)






root.mainloop()
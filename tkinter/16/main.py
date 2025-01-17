# Radio Button in tkinter
from tkinter import *
import tkinter.messagebox as tmsg

def order():
    tmsg.showinfo("Order Recieved",f"We have recieved your order of {var.get()}. Thanks for ordering")

root = Tk()
root.geometry("644x344")
root.title("Khanawala")
f = "lucidia 18 bold"
f1 = "lucidia 12"
var = StringVar()
# var = IntVar()
var.set("Radio")
Label(root,text="What do you want sir?", font=f,padx=20).pack(anchor="w")

radio = Radiobutton(root,text="Dosa",font=f1,padx=30,value="Dosa",variable=var).pack(anchor="w")
radio = Radiobutton(root,text="Idly",font=f1,padx=30,value="Idly",variable=var).pack(anchor="w")
radio = Radiobutton(root,text="Paratha",font=f1,padx=30,value="Paratha",variable=var).pack(anchor="w")
radio = Radiobutton(root,text="Roti",font=f1,padx=30,value="Roti",variable=var).pack(anchor="w")

Button(root,text="Order",command=order).pack()

root.mainloop()
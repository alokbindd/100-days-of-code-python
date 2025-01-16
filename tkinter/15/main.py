# Sliders In Tkinter Using Scale()
from tkinter import *
import tkinter.messagebox as tmsg 
root = Tk()
root.geometry("644x344")
root.title("Slider")
def getdollars():
    tmsg.showinfo("Transferred",f"We have credit {slider1.get()} dollars in your account")
f0 = Frame(root,borderwidth=5,relief=SUNKEN,padx=50,pady=50)
Label(f0,text="How many dollars you want?").pack()
Button(f0,text="Get Dollars",command=getdollars,padx=5,pady=5).pack()
f0.pack(side=TOP,fill="x")
slider1 = Scale(root, from_=0 , to=100, orient=HORIZONTAL,tickinterval=20,length=500,label="Slide me", resolution = 20, fg="blue",bg="pink" )
slider1.set(10)
slider1.pack(side=BOTTOM,fill="x")
root.mainloop()
# Entry Widget & Grid Layout In Tkinter
from tkinter import * 

def getvals():
    print(f"The value of Username is {user_Value.get()}")
    print(f"The value of Password is {pass_value.get()}")

root = Tk()
root.geometry("600x600")

f1= Frame(root, borderwidth=2,bg="White",relief=RIDGE)
f1.pack(side=LEFT,anchor="nw", padx=10,pady=10)

user = Label(f1,text="Username")
user.grid(row=0,column=0,padx=5, pady=5)
Pass = Label(f1,text="Password")
Pass.grid(row=1,column=0,padx=5, pady=5)

# Variable classes in tkinter
# BooleanVar, DoubleVar, IntVar, StringVar

user_Value = StringVar()
pass_value = StringVar()

user_entry = Entry(f1, textvariable=user_Value)
user_entry.grid(row=0,column=1)
pass_entry = Entry(f1, textvariable=pass_value)
pass_entry.grid(row=1,column=1)

Button(f1,text="submit", command=getvals).grid(row=2 ,column=0)







root.mainloop()
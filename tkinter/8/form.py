from tkinter import *

def Fill():
    f = open("merafile.txt","a")
    f.write(f"\n")
    f.write(f"Name:{name_value.get()}")
    f.write(f"\n")
    f.write(f"Age:{Age_value.get()}")
    f.write(f"\n")
    f.write(f"Email:{mail_value.get()}")
    f.write(f"\n")
    

root = Tk()
root.geometry("600x600")
root.title("Gym Form")

f = "Roboto 18 bold"

f1 = Frame(root, borderwidth=3,bg="White", relief=RIDGE)

f2 = Frame(root,borderwidth=2,bg="Pink",relief=SUNKEN)
Label(f2, text="Gym Form", font=f).pack()
f2.pack(side=TOP,anchor="nw",padx=10,pady=10)

Name = Label(f1,text="Name:",font=f).grid(row=0,column=1,padx=5,pady=5)
Age = Label(f1,text="Age:",font=f).grid(row=1,column=1,padx=5,pady=5)
mail = Label(f1,text="Email:",font=f).grid(row=2,column=1,padx=5,pady=5)


name_value = StringVar()
Age_value = IntVar()
mail_value = StringVar()

Name_entry = Entry(f1, textvariable=name_value, font=f)
Name_entry.grid(row=0,column=2)
Age_entry = Entry(f1, textvariable=Age_value, font=f)
Age_entry.grid(row=1,column=2)
mail_entry = Entry(f1, textvariable=mail_value, font=f)
mail_entry.grid(row=2,column=2)

Button(f1,text="Submit",command=Fill,font=f).grid(row=3,column=2)

f1.pack(side=LEFT,anchor="nw",padx=10,pady=10)

root.mainloop()


# f = open("Myfile.txt",'r')
# text = f.read()
# print(text)
# # f.write("Hello My self Alok Bind")
# f.close()
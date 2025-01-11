from tkinter import *

def getvals():
    print("SUBMITTING FORM.................")
    with open("Traveldetails.txt","a") as f:
        f.write(f"\n{name_value.get(),Age_value.get(),Contact_value.get(),Email_value.get(),PaymentMode_value.get(),foodservice_value.get()}")
    print("SUBMITTED")
root = Tk()
root.geometry("644x344")
root.title("Travel Form")
f = "timesnewroman 11"
Label(root,text="Welcome To Alok Travels",font="comicsansms 18 bold", pady=15).grid(row=0,column=3)

name = Label(root,text="Name:",font=f).grid(row=1,column=2)
Age = Label(root,text="Age:",font=f).grid(row=2,column=2)
Contact = Label(root,text="Contact:",font=f).grid(row=3,column=2)
Email = Label(root,text="Email:",font=f).grid(row=4,column=2)
PaymentMode = Label(root,text="Payment Mode:",font=f).grid(row=5,column=2)

name_value = StringVar()
Age_value = StringVar()
Contact_value= StringVar()
Email_value = StringVar()
PaymentMode_value = StringVar()
foodservice_value = IntVar()

Name_entry = Entry(root,textvariable=name_value).grid(row=1,column=3)
Age_entry = Entry(root,textvariable=Age_value).grid(row=2,column=3)
Contact_entry = Entry(root,textvariable=Contact_value).grid(row=3,column=3)
Email_entry = Entry(root,textvariable=Email_value).grid(row=4,column=3)
PaymentMode_entry = Entry(root,textvariable=PaymentMode_value).grid(row=5,column=3)

food = Checkbutton(root,text="Do you want to prebook meal?",font=f,pady=15,variable=foodservice_value).grid(row=6,column=3)

Button(root,text="Submit",font=f,command=getvals).grid(row=7,column=3)

root.mainloop()



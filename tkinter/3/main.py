# Displaying Images Using Label
from tkinter import *
from PIL import Image, ImageTk
root = Tk()
root.geometry("1200x1600")
root.minsize(200,200)
# root.maxsize(700,700)
image = Image.open("D:/Python-lang/tkinter/3/1.png")
photo = ImageTk.PhotoImage(image)
# photo = PhotoImage(file="D:/Python-lang/tkinter/3/4.png")
label = Label(image=photo)
label.pack()
root.mainloop()
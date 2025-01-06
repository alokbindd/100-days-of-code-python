# Label, Geometry, Maxsize & Minsize 
from tkinter import *
root = Tk()

# Width x height
root.geometry("600x600")

# width, height
root.minsize(200,200)
root.maxsize(700,700)
font ="arial",20
label = Label(text="Hello I am alok , this is my first GUI", font=font , foreground="Red")
label.pack()

root.mainloop()
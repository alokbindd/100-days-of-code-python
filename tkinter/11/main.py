from tkinter import *

def alok(event):
    print(f"You Clicked Me at {event.x},{event.y}")

root = Tk()
root.title("Event in tkinter")
root.geometry('644x344')

widget = Button(root,text="Click me")
widget.pack(side=LEFT,anchor="nw")

widget.bind('<Button-1>',alok)
widget.bind('<Double-1>',quit)

root.mainloop()
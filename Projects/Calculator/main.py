from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Calculator")
frm = ttk.Frame(root,padding=100)
frm.grid()
ttk.Label(frm, text="Calculator").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()


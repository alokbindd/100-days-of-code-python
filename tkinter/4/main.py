from tkinter import *
root = Tk()
root.geometry("744x433")
root.title("This GUI is made by Alok")
label = Label(text='''
What is Python?
\nPython is a dynamically typed, General Purpose Programming Language 
\nthat supports an object-oriented programming approach as well as a functional programming approach.
\nPython is also an interpreted and high-level programming language.
\nIt was created by Guido Van Rossum in 1989.
\nFeatures of Python
\nPython is simple and easy to understand.
\nIt is Interpreted and platform-independent which makes debugging very easy.
''',bg="Pink", fg= "Green", font="timesnewroman 11 bold", padx=150,pady=150, borderwidth=5 , relief=SUNKEN)



# label.pack(side=BOTTOM,anchor=NE, fill=X)
label.pack(side=LEFT,anchor=NE,fill=Y)
root.mainloop()
from tkinter import *

root = Tk()
canvas_width = 700
canvas_height = 700
root.geometry(f"{canvas_width}x{canvas_height}")

can_widget = Canvas(root,height=canvas_height,width=canvas_width)
can_widget.pack()

can_widget.create_line(0,0,700,700)
can_widget.create_line(0,700,700,0)

# can_widget.create_rectangle(15,15,500,350,fill="red")
# can_widget.create_arc(5,5,400,400)

can_widget.create_oval(20,20,200,200)


root.mainloop()
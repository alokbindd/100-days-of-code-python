# Python GUI Exercise 1: Solution
from tkinter import *
from PIL import Image , ImageTk
from datetime import datetime,timedelta

def every_100(text):
    final_text = ""
    for i in range(0, len(text)):
        final_text += text[i]
        if i%100 == 0 and i!=0:
            final_text += "\n"
    return final_text

root = Tk()
root.geometry("1000x1300")
root.title("Code with Alok - Newswala")
date = (datetime.today() - timedelta(days=30)).strftime("%d %b %Y")

f0 = Frame(root, width=800, height=15)
Label(text="NewsWalla", font="TimesnewRoman 33 bold").pack()
Label(text=f"{date}", font="TimesnewRoman 13 bold").pack()
f0.pack()
    
texts = []
photos = []
for i in range(0,3):
    with open(f"D:/Python-lang/tkinter/5/" + f"{i+1}.txt", encoding="utf-8") as f :
        text = f.read()
        texts.append(every_100(text))
    
    image = Image.open(f"D:/Python-lang/tkinter/5/" + f"{i+1}.png")
    #TODO: Resize the image 
    image = image.resize((200, 150), Image.ANTIALIAS)
    photos.append(ImageTk.PhotoImage(image))
    
    f = Frame(root, width=800 ,height= 150, pady= 10)
    Label(f, text=texts[i], padx=22 , pady=22).pack(side=LEFT)
    Label(f, image=photos[i], anchor="e", padx=15, pady=15).pack()
    f.pack(anchor="w")











root.mainloop()

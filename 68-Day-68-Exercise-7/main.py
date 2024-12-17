# Write a program to clear the clutter inside a folder on your computer. You should use os module to rename all the png images from 1.png all the way till n.png where n is the number of png files in that folder. Do the same for other file formats. For example:
import os

files = os.listdir("D:/Python-lang/sample")

i = 1
for file in files:
    if file.endswith(".jpg"):
        os.rename(f"D:/Python-lang/sample/{file}",f"D:/Python-lang/sample/{i}.png")
        i = i+1
        print(file)
        





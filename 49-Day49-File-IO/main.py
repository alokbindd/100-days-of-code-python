# WRITING A FILE 
# write (w): This mode opens the file for writing only and creates a new file if the file does not exist.
f = open("Myfile.txt",'w')
# text = f.read()
# print(text)
f.write("Hello My self Alok Bind")
f.close()

#READING A FILE 
# read (r): This mode opens the file for reading only and gives an error if the file does not exist. This is the default mode if no mode is passed as a parameter.

f = open("Myfile.txt",'r')
# f = open("Myfile.txt")
print(f.read())

#APPEND A FILE
# append (a): This mode opens the file for appending only and creates a new file if the file does not exist.
f = open("Myfile.txt",'a')
f.write(". I am pursuing bachelors degree in computer engineering")
f.close()

#create (x): This mode creates a file and gives an error if the file already exists.
# f = open('myfile2.txt','x')
# f.close()

# text (t): Apart from these modes we also need to specify how the file must be handled. t mode is used to handle text files. t refers to the text mode. There is no difference between r and rt or w and wt since text mode is the default. The default mode is 'r' (open for reading text, synonym of 'rt' ).

f = open('Myfile.txt','rt')
print(f.read())

# binary (b): used to handle binary files (images, pdfs, etc).
f = open("myfile2.txt",'rb')
print(f.read())
f.close()

f = open("Python Roadmap - Notes.pdf","rb")
print(f.read())
f.close()

with open('myfile3.txt','r') as f:
    # f.write("Hey, I am fine.")
    print(f.read())
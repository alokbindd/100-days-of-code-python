with open('sample.txt','w') as f:
    f.write('Hello, world!')
    f.seek(5)
    print(f.tell())
    

with open('sample.txt','r') as f:
    f.seek(4)
    print(f.read())

with open('sample2 .txt','w') as f:
    f.write("ello, Myself Alok bind")
    f.truncate(10)
#writelines
# f  = open('merafile.txt','w')
# lines =['Hello, myself Alok Bind','I am pursuing bachelor degree in computer engineering','And i am currently completing 100 days code of python challenge','Its 50th day of my challenge','I am enjoying it ','#U0001F606']
# for line in lines:
#     f.writelines(line + '\n')
# f.close()

#readlines
# f  = open('merafile.txt','r')
# while True:
#     line = f.readline()
#     #print(line)
#     if not line:
#         break
#     print(line)

f = open('merafile2.txt','r')
i = 0 
while True:
    i = i + 1
    line = f.readline()
    if not line:
        break
    m1 = line.split(',')[0]
    m2 = line.split(',')[1]
    m3 = line.split(',')[2]
    print(f"Marks of student {i} is {m1}")
    print(f"Marks of student {i} is {m2}")
    print(f"Marks of student {i} is {m3}")
    print(line)

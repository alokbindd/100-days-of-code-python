for i in range(1,21):
    if(i==11):
        break
    print("5 x", i,"=", 5*i)

for i in range(1,21):
    if(11<=i<=15):
        continue
    print("9 x", i,"=", 9*i)

i = 1
while True:
    print(i)
    i = i+1
    if (i%101==0):
        break

for i in range(1,101,1):
    print(i ,end=" ")
    if(i==50):
        break
    else:
        print("Mississippi")
print("Thank you")

for i in [2,3,9,10,4,6,8,0]:
    if (i%2!=0):
        continue
    print(i)

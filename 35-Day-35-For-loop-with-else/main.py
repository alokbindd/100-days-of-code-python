for i in range(6):
    print(i)
    if i==3:
        break
else:
    print("The loop is over")

i = 1
while i<6:
    print(i)
    i =i+1
else:
    print("The loop is over")

for i in range(6):
    print("iteration no {} in for loop".format(i+1))
else:
    print("over")
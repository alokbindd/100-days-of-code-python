tup = (1,54,"hello",63,"alok",2442,True)
print(type(tup),tup)
print(len(tup))
#accessing element by index
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])
print(tup[4])
print(tup[-4])
print(tup[5])
print(tup[6])

if "hello" in tup:
    print("it is present")
else:
    print("its not present")

tup1 = tup[0:4:2]
print(tup1)

animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[1:8:3])
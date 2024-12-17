marks = [83,39,10,91,99,38,42,64,54,42]
x = "Alok is a programmer"
# index = 0
# for mark in marks:
#     print(mark)
#     if index==4:
#         print("x")
#     index += 1

# for index,mark in enumerate(marks,start=5):
#     print(index,mark)

for index,mark in enumerate(marks):
    print(index,mark)
    if index ==5:
        print(x)

fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits,start=1):
    print(f"{index}:{fruit}")

# Loop over a string and print the index and value of each character
for index,c in enumerate(x):
    print(index,c)
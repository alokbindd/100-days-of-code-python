# a = int(input("Enter value between 3 to 13:"))

# if (a<3 or a>13 or a==quit):
#     raise ValueError("Enter value between 3 to 13:")

# a = input("Enter value between 3 to 13:")
# if a == 'quit':
#     exit()
# elif a.isalpha():
#     print("Input should be integer")
# elif (int(a)<3 or int(a)>13):
#     raise ValueError("Enter value between 3 to 13:")
# elif (a==3 or 13):
#     print("Thank you for your input")

while True:
    a = input("Enter value between 3 to 13: ")

    if a.lower() == 'quit':
        exit()
    elif not a.isdigit():
        print("Input should be an integer")
    else:
        a = int(a)
        if a < 3 or a > 13:
            raise ValueError("Enter value between 3 to 13")
        elif a == 3 or a == 13:
            print("Thank you for your input")
            break

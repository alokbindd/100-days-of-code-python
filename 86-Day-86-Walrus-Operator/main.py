# a = True
# print(a:=False)

# numbers = [1,2,3,4,5,6,7,8,9,10]
# while (n:=len(numbers)) > 0:
#     print(numbers.pop())
# print(n)

# foods = list()
# while True:
#     food = input("What food do you like? ")
#     if food == "quit":
#         break
#     foods.append(food)
# print(foods)

# foods = list()
# while (food:=input("what food do you like? ")) != "quit":
#     foods.append(food)
# print(foods)

# names = ["alok","dhiraj","niraj","Manish"]
# if (name:=input("Enter your name:")) in names:
#     print(f"Hello {name}")
# else:
#     print("Name not fouund")

names = ["alok", "dhiraj", "niraj", "Manish"]
while True:
    if (name := input("Enter your name: ")) in names:
        print(f"Hello {name}")
    else:
        print("Name not found")
        if input("Wanna become a member? yes/no:").lower() == "yes":
            # name = input("Enter Your name")
            names.append(name)
            print(f"Welcome {name}, You are now a member")
        else:
            break

print(names)
 
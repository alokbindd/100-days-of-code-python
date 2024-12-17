# a = input("Enter number:")
# print(f"Multiplication of {a} is:\n")

# try:
#     for i in range(1,11):
#         print(f"{int(a)} X {i} = {int(a)* i}")
# except Exception as e:
#     print(e)
# except ValueError:
#     print("Number entered is not an integer.")

try:
    num = int(input("Enter an integer:"))
    a = [2,8,4,'alok']
    print(a[num])
except ValueError:
    print("Number entered is not an integer.")
except IndexError:
    print("index out of range")
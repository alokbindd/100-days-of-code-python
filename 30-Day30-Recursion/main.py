# Python Recursive Function
# In Python, we know that a function can call other functions. 
# It is even possible for the function to call itself. 
# These types of construct are termed as recursive functions.

# def factorial(n):
#     if (n==0 or n==1):
#         return 1
#     else:
#         return (n * factorial(n-1))

# print(factorial(6))

# def fibo(n):
#     if(n == 0 or n == 1):
#         return 1
#     else:
#         return fibo(n-1) + fibo(n-2)

# n = int(input("Enter number:"))
# print(fibo(n))

n = int(input("Enter Number of Series:"))
n1 = 0
n2 = 1
nx = n2
count = 1

while count <=n:
    print(nx, end=" ")
    count += 1
    n1 = n2
    n2 = nx
    nx = n1+n2
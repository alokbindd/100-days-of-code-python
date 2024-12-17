import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
hours = int(time.strftime('%H'))
# print(hours)
minutes = int(time.strftime('%M'))
# print(minutes)
second = int(time.strftime('%S'))
# print(second)
# https://docs.python.org/3/library/time.html#time.strftime

a = input("Enter Your Name:")
if( 6 <= hours < 12):
    greeting = "Good Morning"
elif( 12 <= hours < 18 ):
    greeting = "Good Afternoon"
elif( 18 <= hours < 22):
    greeting = "Good Evening"
else:
    greeting = "Good Night"

print(greeting +" "+ a)

# Practice exercise to cover/ understand if else statements:
# 1. Leap year checker
# 2. Grading System
# 3. BMI calculator
# 4. Quadratic Equation Solver
# 5. Rock-Paper-Scissors Game
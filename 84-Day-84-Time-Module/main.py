import time

# def usingwhile():
#     i = 0 
#     while i<50000:
#         i = i + 1
#         print(i)

# def usingfor():
#     for i in range(50000):
#         print(i)

# init = time.time()
# usingwhile()
# t1 = f"While loop ran in {time.time()-init} seconds"

# init2 = time.time()
# usingfor()
# t2 = f"For loop ran in {time.time()-init2} seconds"
# print(t1)
# print(t2)

print("start:", time.time())
time.sleep(4)
print("End:", time.time())

t = time.localtime()
# print(t)
f = time.strftime("%d-%m-%Y %I:%M:%S",t)
print(f)

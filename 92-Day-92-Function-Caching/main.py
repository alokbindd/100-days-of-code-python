from functools import lru_cache
import time

# @lru_cache(maxsize=None)
# def fx(n):
#     time.sleep(2)
#     r = n*n
#     return(f"{r}\nDone for {n}")

# print(fx(20))
# print(fx(6))
# print(fx(8))
# print(fx(67))
# print("------------------------------------------------------------------------------------------")
# print(fx(20))
# print(fx(6))
# print(fx(8))
# print(fx(67))
# print("------------------------------------------------------------------------------------------")
# print(fx(1000))

@lru_cache(maxsize=None)
def fibo(n):
    time.sleep(2)
    if n == 0 or n==1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
    
    
print(fibo(3))
print(fibo(5))
print(fibo(10))
print("------------------------------------------------------------------------------------------")
print(fibo(3))
print(fibo(5))
print(fibo(10))
print("------------------------------------------------------------------------------------------")
print(fibo(50))
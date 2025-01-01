import threading
import time 
from concurrent.futures import ThreadPoolExecutor
def func(seconds):
    print(f"sleeping for {seconds} seconds")
    time.sleep(seconds)
    return seconds

def main():
    time1 = time.perf_counter()
    # Normal Code
    # func(3)
    # func(5)
    # func(6)

    # Same code using Threading
    t2 = threading.Thread(target=func,args=[3])
    t1 = threading.Thread(target=func,args=[5])
    t3 = threading.Thread(target=func,args=[6])
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()

    time2 = time.perf_counter()
    print(time2-time1)

def PoolingDemo():
    with ThreadPoolExecutor() as executor:
    #     future1 = executor.submit(func,3)
    #     future2 = executor.submit(func,5)
    #     future3 = executor.submit(func,6)
    #     print(future1.result())
    #     print(future2.result())
    #     print(future3.result())
        l = [3,5,6,8,9]
        results = executor.map(func,l)
        for result in results:
            print(result)
PoolingDemo()
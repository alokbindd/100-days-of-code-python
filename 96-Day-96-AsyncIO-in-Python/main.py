import asyncio
import time
import requests

async def function1():
    print("func1")
    url = "https://images.pexels.com/photos/842711/pexels-photo-842711.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    response = requests.get(url)
    open("pic1.jpg","wb").write(response.content)
    # time.sleep(3)
    return "Alok"

async def function2():
    print("func2")
    url = "https://images.pexels.com/photos/807598/pexels-photo-807598.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    response = requests.get(url)
    open("pic2.jpg","wb").write(response.content)
    # time.sleep(3)
    return "Alok"

async def function3():
    print("func3")
    url = "https://images.pexels.com/photos/33045/lion-wild-africa-african.jpg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    response = requests.get(url)
    open("pic3.jpg","wb").write(response.content)
    # time.sleep(3)
    return "Alok"


async def main():
    # task = asyncio.create_task(function1())
    # await function1()
    # await function2()
    # await function3()
    # return 3
    L = await asyncio.gather(
        function1(),
        function2(),
        function3(),
    )
    print(L)
   
asyncio.run(main())
def greet(fx):
    def mfx(*args,**kwargs):
        print("Hello, world!")
        fx(*args,**kwargs)
        print("Thanks for using this function")
    return mfx


@greet
def hello():
    print("Good Morning")

@greet
def add(x,y):
    print(x + y)

greet(hello)()
greet(add)(5.4,5.6)
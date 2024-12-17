def fun1():
    try:
        l = [11,34,242,24]
        i = int(input("Enter the index:"))
        print(l[i])
        return 1
    except IndexError:
        print("Index out of range")
        return 0
    except ValueError:
        print("Enter a valid number")
    finally:
        print("The is block is always exceuted")

x = fun1()
print(x)
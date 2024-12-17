'''
what is typecasting in python?
Type Casting is a method used to convert one data type into another. It allows us to explicitly

There are two types of typecasting in python
1) Explicit Type Casting: In explicit type casting, we manually convert one data type into(jho hum khud se convert karte hai)
2) Implicit Type Casting: This occurs when we assign value of one data type variable to
another without using any function or operator. Python automatically does this for us.(python  khud kar deta)

'''
#Example of implicit type casting
a = "10"
print(type(a))
b = "50"
print(type(b))
c = a+b
print(c,type(c))
print(int(a)+ int(b))

d = 10.5855
e = -384
print(d+e)
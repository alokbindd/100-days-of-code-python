tuple1 = ("alok","amit","sumit","ankita","ravi",20,32,12,42,"bind")
print(tuple1)

temp = list(tuple1)
print(temp)

temp.append("hello")
print(temp)
# Tuple is immutable but we can add or remove elements from it using methods like append(), extend() and pop(). 

# Tuple is immutable but we can convert it to a mutable object using the list
temp.pop(6)
print(temp)

tuple1 = tuple(temp) # Converting back to tuple 
print(type(tuple1)) 
print(tuple1)

countries = ("Pakistan", "Afghanistan", "Bangladesh", "SriLanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries + countries2
print(southEastAsia)

tuple2 = (8,53,35,2,7,43,7,3,8,7,3)
print(sorted(tuple2))
print(max(tuple2))
print(min(tuple2))
print(tuple2.count(7))
print(tuple2.index(7,8,10))

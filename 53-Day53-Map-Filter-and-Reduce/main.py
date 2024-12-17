# MAP
# def cube(x):
#     return x**3

# print(cube(2))

l = [1,2,3,4,6,5,8,6,9,5]
# sumo = 0
# for num in l:
#     sumo =  sumo+ num
#     sumo += num
# print(sumo)
# print(sum(l))
# newl=[]
# for item in l:
#     newl.append(cube(item))
# print(newl)

newl = list(map(lambda x: x**3 ,l))
print(newl)

# FILTER
def filter_function(x):
    return x > 3

newnewl = filter(filter_function,l)
print(list(newnewl))

newnewl1 = filter(lambda x: x%2==0 ,l)
print(list(newnewl1))

# REDUCE
from functools import reduce

sum = reduce(lambda x,y:x+y,l)
print(sum)

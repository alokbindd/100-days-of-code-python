# isdisjoint():
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print(cities.isdisjoint(cities2))

# issuperset():
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}
print(cities.issuperset(cities2))
cities3 = {"Seoul", "Madrid","Kabul"}
print(cities.issuperset(cities3))

# issubset():
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Delhi", "Madrid"}
print(cities2.issubset(cities))

# add()
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.add("Rabale")
print(cities)

# update()
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2={"rable","airoli","vashi"}
cities.update(cities2)
print(cities)

# remove()/discard()
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Tokyo")
print(cities)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.discard("alok")
print(cities)

# clear():
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.clear()
print(cities)

# del
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
del cities
print(cities)
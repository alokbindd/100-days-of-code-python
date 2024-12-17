# Joining Sets
# I. union() and update():
cities = {'new mumbai','mumbai','thane','delhi','lucknow'}
cities2 = {'new york','california','delhi','thane','goa'}
cities3 = cities.union(cities2)
print("union is:",cities3)

cities.update(cities2)
print("update :",cities)

# II. intersection and intersection_update():
cities = {'new mumbai','mumbai','thane','delhi','lucknow'}
cities2 = {'new york','california','delhi','thane','goa'}
cities3 = cities.intersection(cities2)
print("intersection :",cities3)

cities.intersection_update(cities2)
print("intersection_update :",cities)

# III. symmetric_difference and symmetric_difference_update():
cities = {'new mumbai','mumbai','thane','delhi','lucknow'}
cities2 = {'new york','california','delhi','thane','goa'}
cities3 = cities.symmetric_difference(cities2)
print("symmetric_difference: ",cities3)

cities.symmetric_difference_update(cities2)
print("symmetric_difference_update: ",cities)

# IV. difference() and difference_update():
cities = {'new mumbai','mumbai','thane','delhi','lucknow'}
cities2 = {'new york','california','delhi','thane','goa'}
cities3 = cities.difference(cities2)
print(cities3)

cities.difference_update(cities2)
print(cities)

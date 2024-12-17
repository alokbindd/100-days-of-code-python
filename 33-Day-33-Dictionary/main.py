dict = {
    "Name":"alok",
    "Class" : "BE",
    "Roll no" : 9
}

print(dict["Name"])
print(dict.get("Name"))

print(dict.keys())
print(dict.values())
# print(dict.items())

for key in dict.keys():
    # print(dict[key])
    print(f"the corresponding value to key {key} is {dict[key]}")

print(dict.items())
for key,values in dict.items():
    print(f"the corresponding value to key {key} is {values}")
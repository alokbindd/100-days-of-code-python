letter = "hey my name is {1} and i live in {0}"
country = "India"
name = "Alok"
# print(letter.format(name, country))
# print(letter.format(country,name))
letter = f"hey my name is {name} and i live in {country}"
print(letter)

# txt = "For only {price:.2f} dollars!"
# print(txt.format(price = 49))
# val = 'Geeks'  
# print(f"{val}for{val} is a portal for {val}.")  
# name = 'Tushar'  
# age = 23  
# print(f"Hello, My name is {name} and I'm {age} years old.")  

print(f"{2 * 30}")  
letter = f"we like f string like this :hey my name is {{name}} and i live in {{country}}"
print(letter)

txt ="the actual price is {price:.2f} of toy"
print(txt.format(price = 50.684439))
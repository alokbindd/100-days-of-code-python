a = "Alok Bind 01"
print(a.upper()) 
# This will convert the string 'Alok Bind' to uppercase letters and print
print(a.lower())  
# This will convert the string 'Alok Bind' to lowercase letters and print
print(a.strip(" "))
# This function returns a copy of the string with leading/trailing characters removed (whitespace is not removed). 
# If no argument is passed, it removes all kinds of spaces.   
print(a.rstrip(""))
# It removes characters from right side of the string till it encounters specified character or end of the string. In this case, it removes 'd' from right side of the string.
print(a.replace("Alok","Amit"))
# It replaces every occurrence of first argument with second argument in the given string
print(a.split())
# It splits the string into list of words if there are any spaces between them.
b = "this is my REPL"
print(b.capitalize())
# It capitalizes only the first letter of the string and make rest as small.
print(a.center(50))
print(a.center(50,"!"))
# It centers the string with specified length by adding extra space on both sides.
print(len(a))
print(len(a.center(50)))
print(b.count("i"))
print(a.count("A"))
str1 = b.count("i")
print(str1)

print(b.endswith("REPL"))
# Returns True if the string ends with the specified value (here "REPL"). Otherwise False.
print(b.endswith("repl"))

print(a.find("d"))
print(a.find("e"))
# It returns the index position where the substring starts.

str1 = "He's name is Dan. Dan is an honest man."
print(str1.index("Dan"))
# str1 = "He's name is Dan. Dan is an honest man."
# print(str1.index("Daniel"))
# It returns the first occurrence of the specified value. Raises an exception if not found.
# a= "alok12"
print(a.isalnum())
str1 = "WelcomeToTheConsole"
print(str1.isalnum())
# Checks whether the string contains alphanumeric characters or not. Returns True or False.

str1 = "Welcome"
print(str1.isalpha())
# Checks whether the string contains alphabetical characters only. Returns True or False.

print(a.islower())
str1 = "hello world"
print(str1.islower())
# Checks whether the string contains lowercase letters only. Returns True or False.

str1 = "We wish you a Merry Christmas \n"
print(str1.isprintable())
str1 = "We wish you a Merry Christmas"
print(str1.isprintable())
# Checks whether all characters in the string are printable. Returns True or False.

str1 = "        "       #using Spacebar
print(str1.isspace())
str2 = "        "       #using Tab
print(str2.isspace())
# Checks whether the string consists of whitespaces only. Returns True or False.

print(a.istitle())
print(b.istitle())
# Checks whether the string consists of words that have both upper and title case characters, such as

str1 = "WORLD HEALTH ORGANIZATION" 
print(str1.isupper())
# Checks whether the string consists of uppercase letters only. Returns True or False.

str1 = "Python is a Interpreted Language" 
print(str1.startswith("Python"))
# Checks whether the string starts with the specified prefix. Returns True or False.

print(a.swapcase())
# Convert uppercase characters to lowercase and lowercase characters to uppercase.

print(b.title())
# Converts first character of each word to Upper Case (Capital) Letter and remaining
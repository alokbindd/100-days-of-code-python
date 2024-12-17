import os
folders = os.listdir("D:/Python-lang/46-Day-46-os-Module/Data")
# print(folders)

for folder in folders:
    print(folder)
    print(os.listdir(f"D:/Python-lang/46-Day-46-os-Module/Data/{folder}"))

print(os.getcwd())
os.chdir("D:/Python-lang/46-Day-46-os-Module")
print(os.getcwd())
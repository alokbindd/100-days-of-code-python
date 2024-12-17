import os
path = "D:/Python-lang/46-Day-46-os-Module/Data" 

# if(not os.path.exists(path)):
#     os.mkdir(path)

for i in range(1,101):
    os.mkdir(f"D:/Python-lang/46-Day-46-os-Module/Data/Tutorial {i}")
    # os.rename(f"D:/Python-lang/46-Day-46-os-Module/Data/Day {i+1}",f"D:/Python-lang/46-Day-46-os-Module/Data/Tutorial {i}")

# for i in range(1,101):  
#     os.rmdir(f"D:/Python-lang/46-Day-46-os-Module/Data/Tutorial {i}")
    
import shutil


path = "D:/Python-lang/87-Day-87-Shutil-Module"

# Use an ignore function to exclude existing "tutorial" folders
def ignore_tutorials(dir,contents):
    return [item for item in contents if item.startswith('tutorial')]

for i in range(1, 5):
    shutil.copytree(path, f'{path}/tutorial{i}', ignore=ignore_tutorials)

import shutil
import os

path ="D:/Python-lang/87-Day-87-Shutil-Module"
# Copy file
# shutil.copy(path + '/main.py', path + '/main1.py')
# os.mkdir(path + '/Sample')
# os.getcwd()

# shutil.copy2(path + "/main.py", path + "/sample/main.py")

# shutil.copytree(path + '/sample',path + '/sample2')

# shutil.move(path + '/main1.py',path + '/sample/main1.py')

# shutil.move(path + '/sample2',path + '/sample')

# shutil.copytree(path + '/sample/sample2', path + '/sample1')

# shutil.rmtree(path+ '/sample1')

# shutil.rmtree('87-Day-87-Shutil-Moduletutorial{i}')

for i in range(1,5):
    shutil.copytree( path ,f'D:/Python-lang/sample/tutorial{i}')



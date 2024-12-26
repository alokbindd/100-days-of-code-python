import shutil
import os

path ="D:/Python-lang/87-Day-87-Shutil-Module"
# Copy file
shutil.copy(path + '/main.py', path + '/main1.py')
os.mkdir(path + '/Sample')
os.getcwd()
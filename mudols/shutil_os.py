import os
import shutil
import send2trash
f = open('practice.txt','w+')#if the file dont exist, open a new file in the name, if exist, opens the file
f.write('this is a test string')
f.close()
os.getcwd()#diractory location  
os.listdir()#show all files in this diractory
os.listdir('c:\\Users') #giving back item in c:\\Users
shutil.move('practice.txt', 'Desktop')#moves src(practice.txt) to a diffrent location (desktop)
shutil.move('practice.txt', 'os.getcwd')#moves src(practice.txt) to this diractory
send2trash.send2trash('practice.txt')#throws the file to trash(not complitly deleting it)

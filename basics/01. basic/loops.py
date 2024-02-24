#for loops

from inspect import stack
from tkinter import N


name = "amit"
for letter in name:
    print(letter)
print("\n")

num = len(name)#giving the length of the string

for i in range(0,num):#running for 0 to num(the length of the string)
    if(i == "i"):
        pass  
    if(i == 0):
        break  
    print(i)
print("\n")

#whileloops
number2=0
while number2 != -1:
        number2 = input('enter numbr:')
        print('not the right number, try again.')
        print('\n')
        if number2 == 10:
            print('congrats! you guessed the sicret number but not the right number but its ok!')
            break
print('good job!')

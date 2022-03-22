#lists 

from __future__ import barry_as_FLUFL
from ast import While
from csv import list_dialects


names = ["lea","yuval","ran","dan"]
num = len(names)
print(num)
names.append("peery")
print(names)
names.pop()
print(names)
print(names[0])
print(names[-1])
nums = [1,2,3,4,5]
names = nums+names
print(names)
names.remove(1)
print(names[0])

#dict







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


#class
class worker:
    name = ""
    id = 0
    hours = 0.0
    age = 0
    perhour=0
    gender = ""

    def __init__(self,name,id,hours,age,perhour,gender):
        self.name =name 
        self.age =age
        self.hours= hours
        self.perhour = perhour
        self.gender =gender
    

    def changegpa (self,newperhour):
        self.perhour = newperhour

    def addHours(self,hours):
        selfhours = self.addHours+ hours
    
    def salery(self):
        return self.perhour*self.hours

    def SaleryWithBonus(self,bonusprecent):
        bonusprecnt = bonusprecent/100
        salery = self.hours*self.perhour 
        salery = salery +salery*bonusprecent
    
    
    



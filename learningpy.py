#for loops


from tkinter import N


name = "amit"
for letter in name:
    print(letter)
print("\n")

num = len(name)#giving the length of the string

for i in range(0,num):#running for 0 to num(the length of the string)
    print(i)
print("\n")


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
    
    def salery():
        return self.perhour*self.hours

    def SaleryWithBonus(self,bonusprecent):
        bonusprecnt = bonusprecent/100
        salery = self.hours*self.perhour 
        salery = salery +salery*bonusprecent
    
    
    



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
        self.id = id
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
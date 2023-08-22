class Vector:

    def __init__(self, x, y):
         self.x = x
         self.y = y


    def __add__(self , other): #makes the + work by defining what will happend when i try to add objects together
         return Vector(self.x + other.x , self.y +other.y)


    def __repr__(self):
         return f"x:{self.x}, y:{self.y}"

v1 = (5,3)
v2 = (10,60)
v3 = v1+v2
print(v3)

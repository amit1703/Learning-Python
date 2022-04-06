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

def square (num):
    return num**2

my_list = [1,2,3,4,5,6]
for item in map(square,my_list):
    print(item)
new_list = list(map(square,my_list))

def even (num):
    return num%2 == 0 

for item in filter(even,my_list):
    print(item)
new_list = list(filter(even,my_list))
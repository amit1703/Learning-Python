square = lambda num: num**2
my_num = [1,2,3,4,5,6,7]
for item in map(lambda num:num**2,my_num):
    print(item)
names = ['amit','andy','tahel']
my_list = list(map(lambda x:x[::-1],names))
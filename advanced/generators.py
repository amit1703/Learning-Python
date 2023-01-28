def create_cubes(n):
    for x in range(n):
        yield x**3
    
def fibo_sqnce(n):
    a = 1
    b = 1
    for i in range(n):
        yield a 
        a,b = b,a+b
    
for x in fibo_sqnce(10):
    print(x)

def simple_gen():
    for x in range (3):
        yield x 

g = simple_gen() 
print(next(g))# 0
print(next(g))# 1
print(next(g))# 2 


s = 'hello'
s_iter = iter(s)
next(s_iter)#h 
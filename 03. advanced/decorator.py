def new_decorator(original_func):
        
        def wrap_func():
            
            print('some extra code before the original fun')
            
            original_func()
            
            print('after')
        return wrap_func
    
@new_decorator 
def func_needs_decorator():
    print('i want to be decorated!')
func_needs_decorator()



#another example:





def my_decor(func):
    
    def wrapper(*args):#passes the arguments from the original function
        print("im decorating")
        func(*args)
    
    return wrapper

@my_decor
def hello_world(name):
    print(f'hello {name}!')
hello_world('amit')
def new_decorator(original_func):
        
        def wrap_func():
            
            print('some extra code before the original fun')
            
            original_func()
            
            print('after')
        return wrap_func
    
@new_decorator 
def func_needs_decorator():
    print('i want to be decorated!')


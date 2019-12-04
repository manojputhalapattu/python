
def something(a,b):
    print(a/b)
    
    
def decorator_1(func):

    def decorator_2(a,b):
        if a<b:
            a,b=b,a
            
        return func(a,b)
    
    return decorator_2


something1=decorator_1(something)
    




something1(5,10)
f=something1(5,10)
print(f)

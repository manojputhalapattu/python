def something(fbi):
    a=0
    b=1
    print(a)
    print(b)
    for e in range(2,fbi):
        
        c=a+b
        a=b
        b=c
        if c<=fbi:
            print(c)
        else:
            break
             
    
   
    


x=int(input("enter the no of fabinocci numbers to be printed"))
something(x)

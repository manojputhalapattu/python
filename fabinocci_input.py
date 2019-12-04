def something(fbi):
    a=0
    b=1
    if fbi==1:
        print(a)
        
    elif  fbi<=0:
        print("no numbers to be printed")
    else:
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

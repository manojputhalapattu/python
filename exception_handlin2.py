a=2;
b=0;
try:
    print("resource opend")
    print(a/b)
except Exception:
    print("cant divide by zero")
    print("resource closed")
    
#here if the resource was closed in the try block it self then the opned resource will not
#get closed as in we should always close the resorce that we have opned
#so we have placed that resource closing in the exception block
    #then what if we have no zero error?
            #the resource wiil be opned
    #for solution we use the finally block
    

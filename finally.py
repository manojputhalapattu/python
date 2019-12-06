a=2;
b=0;
try:
    print("resource opend")
    print(a/b)
except Exception:
    print("cant divide by zero")
finally:
    print("resource closed")

#here the finally block will be executed irrespectvie of the try and the catch blockes

    

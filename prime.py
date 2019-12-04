num=int(input("enter the number to check prime or not "))
for i in range(2,num):
    if num%i==0:
        print("not a prime number")
        break
else:
    print("prime")
        

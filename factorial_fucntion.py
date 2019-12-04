def something(n):
    z=1
    for e in range(1,n+1):
        z=z*e
        
    return z

x=int(input("enter the number to find the factorial of"))

result=something(x)

print(result)


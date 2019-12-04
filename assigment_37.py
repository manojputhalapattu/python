def something(y):
    five=0
    less=0
    for e in y:
        if len(e)>=5:
            five+=1
        else:
            less+=1
    return five,less 

x=int(input("enter the number of names to check"))
y=[]
for i in range(x):
    z=input("enter the next name")
    b=y.append(z)
print(y)
something(y)
five,less=something(y)
print(five)
print(less)
    

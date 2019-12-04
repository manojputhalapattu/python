from array import *

arr=array('i',[])

n=int(input("enter the length of the array"))

for i in range(n):
    x=int(input("enter the next value"))
    arr.append(x)


print(arr)


k=int(input("enter the index to be deleted "))
del arr[k]

print(arr)
    

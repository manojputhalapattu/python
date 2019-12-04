from array import *

arr=array('i',[])

n=int(input("enter the length of the array"))

for i in range(n):
    x=int(input("enter the next value"))
    arr.append(x)


print(arr)

y=int(input("enter the element to search"))

for e in range(n):
    if arr[e]==y:
        print(arr[e])
        break
else:
    print("element not found")

print(arr.index(y))

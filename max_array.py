from array import *
arr=array('i',[11,22,440,55])
max=0
for i in range(len(arr)):
    if arr[i]>max:
        max=arr[i]
print(max)

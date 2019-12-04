from array import *
arr1=array('i',[3,4,5])
arr2=array('i',[4,5,6])
arr3=array('i',[])
for i in range(len(arr1)):
    arr3=arr1[i]+arr2[i]
    print(arr3)

from array import *
arr1=array('i',[1,2,3])
arr2=array('i',[3,4,5])
arr3=array('i',[])
for e in range(len(arr1)):
    arr3.append(arr1[e]+arr2[e])
    print(arr3)
    

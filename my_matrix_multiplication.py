arr1=[[1,2,3],
      [3,4,5],
      [5,6,1]]
arr2=[[3,4,5],
      [6,1,2],
      [4,5,6]]
arr3=[[0,0,0],
      [0,0,0],
      [0,0,0]]
for b in range(len(arr1)):
    for c in range(len(arr2[0])):
                   for h in range(len(arr2)):
                       
                       arr3[b][c] +=arr1[b][h]*arr2[h][c]
for j in arr3:
                   print(j)

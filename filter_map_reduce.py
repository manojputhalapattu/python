from functools import reduce

nums=[1,2,3,4,5,6,7,8,9]
evens=list(filter(lambda e:e%2==0,nums))
print(evens)
doubles=list(map(lambda x:x*2,evens))
print(doubles)
#sum=reduce(lambda c,n=c+n,doubles)
#print(sum)

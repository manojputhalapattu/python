
def oldd(lst):
    even=0
    odd=0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
            
    return even,odd

lst=[20,31,55,67,34,5,6,7,9]  
even,odd = oldd(lst)



print(even)
print(odd)

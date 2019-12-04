import sys
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())
i=0
def manoj():
    global i
    i+=1
    print("hello",i)
    return manoj()


manoj()

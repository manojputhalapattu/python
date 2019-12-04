a=10
def something():
    a=9
    print("in_fun_",a)
    globals()["a"]=15
something()
print("outside",a)

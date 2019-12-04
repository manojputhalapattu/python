a=10
def something():
    global a
    a=15
    print("in_fun",a)
something()
print(a)

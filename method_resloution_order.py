class a():
    def __init__(self):
        print("init in a ")
    def feture1(self):
        print("feature 1 working")
class b():
    def __init__(self):
        print("init in b")
class c(a,b):
    def __init__(self):
        super().__init__()
        print("init in c")
c1=c()
#here when we call super we both have class a, b and c how python knows which one to call first?
#here we have MRO FROM LEFT TO RIGHT

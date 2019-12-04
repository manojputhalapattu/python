class a():
    def __init__(self):
        print("init in a ")
    def feture1(self):
        print("feature 1 working")
class b(a):
    def __init__(self):
        super().__init__()
        print("init in b")

b1=b()# object creation for class b
# here syper keyword helps to invoke the __init__ in both class a and b
#object b1 invokes------> constructor __init__ in class b which invokes----->super keyword
# then that super invokes  ------>init in a 

class a():
    def __init__(self):
        print("init from a")
    def add(self,m1,m2):
        m3=m1.self+m2.self
        print(m3)
class b(a):
    def __init__(self):
        print("init from b")

b1=b()# object creation for the class b
#here python checks for the init in b
                                 # if b exists
                                       #======> print init in b
                                 # else
                                       #======> print init in a since inherited 
                                      

    
        

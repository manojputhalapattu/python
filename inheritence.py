class a:
    def manoj(self):
        print("from class a ")
class b(a):
    def pillai(self):
        print("from class b ")

a1=b()#object for class b
a1.manoj()
#here we are creating object for the class b and we were calling the methods from the class a with the inheritance 

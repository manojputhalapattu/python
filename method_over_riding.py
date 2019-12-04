class a():
    def show(self):
        print("show in a")
class b(a):
    def show(self):
        print("show in b")
b1=b()
b1.show()

# here we have created 2 methods with same name(of course in 2 classes)


# but when ever we call b1.show it invokes the show in b if present

# else it will o and check for method in a since we have inherited

# that show method in class a will be over rided by show method of class b now

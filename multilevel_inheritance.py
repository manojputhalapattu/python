class A:
    def feature1(self):
        print("feature 1 from class A")
    def feature2(self):
        print("feature 2 from class A")
class B(A):
    def feature3(self):
        print("feature 3 from class B")
    def feature4(self):
        print("feature 4 from class B")
class C(B):
    def feature5(self):
        print("feature 5 from class C")

c1=C() #object for the class C 
c1.feature1()
c1.feature4()
# here from the object c1 we are calling methods of other class A and B
# at the same time 

class computer:
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
    def manoj(self):
        print("this is config",self.cpu,self.ram)

com1=computer("i5","16gb ram")
com2=computer("i7","8gb ram")

com1.manoj()
com2.manoj()

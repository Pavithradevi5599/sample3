#
class Constructor:
    def __init__(self,a,b):
        self.a1=a
        self.b1=b

    def add(self):
        c=self.a1+self.b1
        print("Addition:",c)


obj=Constructor(10,20)
obj.add()
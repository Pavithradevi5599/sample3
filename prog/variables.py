class Mark:

    # class variable
    maths=100

    def __init__(self):
        # instance variable
        self.tamil=90
        self.english=80

    def record(self):
        print("Tamil:",self.tamil)
        print("English:",self.english)
        print("Maths:",self.maths)


obj=Mark()
obj2=Mark()

Mark.maths=40

obj.tamil=85
obj.english=70

obj2.tamil=55
obj2.english=40

obj.record()
obj2.record()
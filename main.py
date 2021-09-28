class Man:
    def __init__(self,name):
        self.name = name
        print("initialized!")

    def hello(self):
        print("Hello "+self.name+"!")

m = Man("David")
m.hello()
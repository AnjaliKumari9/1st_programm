class Test:
    a=10
    def __init__(self,a):
        self.a=a
        return
    

    def display(self):
        a=30
        print("method-a:",a)
        print("object-a:",self.a)
        print("class-a:",Test.a)
        return
    
obj=Test(20)
obj.display()
       
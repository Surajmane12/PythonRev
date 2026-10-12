class Outer:
    
    def __init__(self):
        self.name="Outer class!!"
    
    class Inner:
        def __init__(self):
            self.name="Inner class!!"

        def display(self):
            print("This is inner class..")

outer=Outer()
inner=outer.Inner()
print(outer.name)
print(inner.display())
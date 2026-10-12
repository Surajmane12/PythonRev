class Person:

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def getData(self):
        return f"Hii! {self.name} with age: {self.age}"

class Child(Person):

    def __init__(self, name,age,skill):
        # Person.__init__(self,name,age)
        super().__init__(name,age) 
        # To access parent class all data above by Parent class Name OR by super() keyword
        self.skill=skill
        self.age=age

    def newData(self):
        return f"Hey {self.name} with {self.age} and skill {self.skill}"

    
obj = Child("Aaditya","23","PY")
print(obj.newData())

    
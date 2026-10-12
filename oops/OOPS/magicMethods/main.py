
class Person:

    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.skills=[]

    def __str__(self):
        return f"{self.name} with {self.age}"

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"

    def __eq__(self,other):
        return self.name==other.name

    def __add__(self,other):
        return self.age + other.age

    def __contains__(self, skill):
        return skill in self.skills
    
    def addSkill(self,skill):
        self.skills.append(skill)

    def __call__(self,factor):
        return self.age + factor

    


obj = Person("Suraj",22)
obj2 = Person("Rahul",21)

print(obj+obj2) # invokes __add__ method
print(obj)      # invokes __str__ method
print(repr(obj)) # invokes __repr__ method
print(obj==obj2) # invokes the __eq__ method


obj.addSkill("Python")
obj.addSkill("React")
obj.addSkill("Node")

print("React" in obj) # invokes __contains__ method

print(obj(10)) # invokes __call__ method




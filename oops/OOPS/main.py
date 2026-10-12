class Car:

    year="2027" # Class Property

    def __init__(self,name,model):
        # Instance Peroperty
        self.name=name
        self.model=model

    def getData(self):
        return f"Car: {self.name} and Model: {self.model}"
    
obj = Car("MAHINDRA","XUV")

obj2 = Car("Toyota","Fortuner")

# del obj2.name  // To Delete the attri for the obj reference

print(obj2.getData())

print(obj.getData())
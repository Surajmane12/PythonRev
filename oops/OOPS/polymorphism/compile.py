class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    return "Drive!"

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    return "Sail!"

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    return "Fly!"

car1 = Car("Ford", "Mustang")       
boat1 = Boat("Ibiza", "Touring 20") 
plane1 = Plane("Boeing", "747")     


for x in (car1, boat1, plane1):
  print(x.move())
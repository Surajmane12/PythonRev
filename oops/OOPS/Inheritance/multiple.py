class PersonalDetails():
    def __init__(self,name,age,**kwargs):
        super().__init__(**kwargs)
        self.name=name
        self.age=age

    def showPersonalDetails(self):
        return f"{self.name}, Age: {self.age}"

class WorkDetails():
    def __init__(self,empId, department,**kwargs):
        super().__init__(**kwargs)
        self.empId=empId
        self.department=department

    def showWorkDetails(self):
        return f"Employee ID: {self.empId} and Department: {self.department}"

class Employee(PersonalDetails,WorkDetails):
    def __init__(self,name,age,empId,department):
       super().__init__(
           name=name,
           age=age,
           empId=empId,
           department=department
       )

    def showEmployeDetails(self):
        return f"""
                   Name: {self.name}, 
                   Age: {self.age} 
                   Employee ID: {self.empId}, 
                   Department: {self.department}
                """
obj = Employee("Aaditya",24,101,"QA")

print(obj.showEmployeDetails())
print(obj.showWorkDetails())
print(obj.showPersonalDetails())
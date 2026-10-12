class User:
    def __init__(self,name,email):
        self.name=name
        self.email=email

    def showUserDetails(self):
        return( f"Name: {self.name}\n"
                f"Email: {self.email}")

class Student(User):
    def __init__(self,name,email,course):
        super().__init__(name,email)
        self.course=course

    def showCourse(self):
        return f"Course is: {self.course}"

class PremiumStudent(Student):
    def __init__(self,name,email,course,discount):
        super().__init__(name,email,course)
        self.discount=discount

    def showDiscount(self):
        return f"Discount: {self.discount}"

obj = PremiumStudent("Suraj","suraj@gmail.com","AI",70)
print(obj.showUserDetails())
print(obj.showCourse())
print(obj.showDiscount())
    
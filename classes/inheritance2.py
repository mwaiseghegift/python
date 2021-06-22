
class Lecturer:
    def __init__(self, firstName, lastName, department):
        self.firstName = firstName
        self.lastName = lastName
        self.department = department
    
    def getProperties(self):
        objects = [self.firstName, self.lastName, self.department]
        return objects

class Student(Lecturer):
    def __init__(self, firstName, lastName, department, year):
        super().__init__(firstName, lastName, department)
        self.year = year
        
    def getProperties(self):
        objects = [self.firstName, self.lastName, self.department, self.year]
        return super().getProperties()

lec1 = Lecturer("Mr", "Kariuki", "SPAS")
student1 = Student("Mr", "Mwaiseghe", "SPAS", 2)
for obj in lec1.getProperties():
    print(obj)
    
print("\n\n")

for obj in student1.getProperties():
    print(obj)
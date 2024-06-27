class Person:
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname
    def printname(self):
        print(self.firstName, self.lastName)


class Student(Person):
    def __init__(self, fname, lname, graduationYear):
        super().__init__(fname, lname)
        self.graduationyear = graduationYear
    def printname(self):
        print(self.firstName, self.lastName, self.graduationyear)

x = Student("Aditya", "Chatap", 2024)
x.printname()
print(x.graduationyear)


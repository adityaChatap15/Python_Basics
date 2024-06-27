class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        # length = len(self.marks)
        for val in self.marks:
            sum += val
        print("Hi", self.name, "average marks is", sum/len(self.marks))




s1 = Student("Aditya", [20, 30, 40])
s1.get_avg()

s1.name = "Ayush"
s1.get_avg()
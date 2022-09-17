"""Python Object-Oriented Programming Exercise - Classes and Objects Exercises"""


class Students:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade


class Staff:
    def __init__(self, name, age, role, dept, salary):
        self.name = name
        self.age = age
        self.role = role
        self.dept = dept
        self.__salary = salary

    def show_details(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Role:", self.role)
        print("Department", self.dept)


class Teacher(Staff):
    def __init__(self, name, age, dept, salary, role="Teacher"):
        super().__init__(name, age, role, dept, salary)



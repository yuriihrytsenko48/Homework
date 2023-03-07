"""
Task 1

School

Make a class structure in python representing people at school. Make a base
class called Person, a class called Student, and another one called Teacher.
Try to find as many methods and attributes as you can which belong to different
classes, and keep in mind which are common and which are not. For example, the
name should be a Person attribute, while salary should only be available to the
teacher.
"""

class Person:

    def __init__(self, fullname, age, sex, ):
        self.fullname = fullname
        self.age = age
        self.sex = sex

    def info_representation(self):
        x = self.__dict__
        for values in x.values():
            print(values)


class Student(Person):

    def __init__(self, fullname, age, sex, grade, lessons, average_scale):
        super().__init__(fullname, age, sex,)
        self.grade = grade
        self.lessons = lessons
        self.average_scale = average_scale


class Teacher(Person):

    def __init__(self, fullname, age, sex, salary, lessons):
        super().__init__(fullname, age, sex)
        self.salary = salary
        self.lessons = lessons


chris = Person("Chris", 20, "man")
zack = Teacher("Zack", 28, "man", 20000, "Chemistry")
derek = Student("Derek", 15, "man", 9, ["Physic", "Math", "language"], 9.9)


persons = [chris, zack, derek]

for person in persons:
    person.info_representation()
    print("\n")

"""

Task 2

Doggy age

Create a class Dog with class attribute `age_factor` equals to 7.
Make __init__() which takes values for a dog’s age. Then create a method
`human_age` which returns the dog’s age in human equivalent.

"""

class Dog:

    def __init__(self, surname, age):

        self.surname = surname
        self.age = age
        self.human_years = str(int(age) * 7)

    def human_age(self):
        print(f"The {self.surname} has {self.human_years} human years.")


lacky = Dog("Lacky", "7")

lacky.human_age()

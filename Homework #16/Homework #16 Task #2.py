"""
Task 2

Mathematician

Implement a class Mathematician which is a helper class for doing
math operations on lists

The class doesn't take any attributes and only has methods:

square_nums (takes a list of integers and returns the list of squares)
remove_positives (takes a list of integers and returns it without positive
numbers
filter_leaps (takes a list of dates (integers) and removes those that are
not 'leap years'
"""


class Mathematician:

    def square_nums(self, list_of_numbers):
        return [i ** 2 for i in list_of_numbers]

    def remove_positives(self, list_of_numbers):
        return [i for i in list_of_numbers if i < 0]

    def filter_leaps(self, list_of_numbers):
        return [i for i in list_of_numbers if i % 4 == 0]


m = Mathematician()

list1 = [7, 11, 5, 4]
list2 = [26, -11, -8, 13, -90]
list3 = [2001, 1884, 1995, 2003, 2020]

print(m.square_nums(list1) == [49, 121, 25, 16])
print(m.remove_positives(list2) == [-11, -8, -90])
print(m.filter_leaps(list3) == [1884, 2020])

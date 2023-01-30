"""
Task 2
Exclusive common numbers.

Generate 2 lists with the length of 10 with random integers from 1 to 10,
 and make a third list containing the common
 integers between the 2 initial lists without any duplicates.

Constraints: use only while loop and random module to generate numbers
"""

from random import randint

number_list1 = []
number_list2 = []
number_list3 = []

while len(number_list1) <= 10 and len(number_list2) <= 10:
    number_list1.append(randint(0, 10))
    number_list2.append(randint(0, 10))

print(number_list1)
print(number_list2)

for number in number_list1:
    if number in number_list2:
        number_list3.append(number)
        while number in number_list2:
            number_list2.remove(number)

print(number_list3)

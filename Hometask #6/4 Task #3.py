"""
Task 3
Extracting numbers.

Make a list that contains all integers from 1 to 100,
then find all integers from the list that are divisible by 7
but not a multiple of 5, and store them in a separate list.
Finally, print the list.

Constraint: use only while loop for iteration
"""


numbers = [number for number in range(1, 101)]
seeking_numbers = []

while numbers:
    test_number = numbers.pop()
    if test_number % 7 == 0 and not test_number % 5 == 0:
        seeking_numbers.append(test_number)


print(seeking_numbers)

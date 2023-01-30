
"""
Task 3

List comprehension exercise

Use a list comprehension to make a list containing tuples (i, j)
where `i` goes from 1 to 10 and `j` is corresponding to `i` squared.
"""

tuples = [(i, j**2) for i in range(1, 11) for j in range(1, 11)]

print(tuples)

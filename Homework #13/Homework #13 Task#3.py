"""
Task 3

Write a function called `choose_func` which takes a list of nums and 2
callback functions. If all nums inside the list are positive,
execute the first function on that list and return the result of it.
Otherwise, return the result of the second one.
"""


def square_nums(nums):
    return [num ** 2 for num in nums]


def remove_negatives(nums):
    return [num for num in nums if num > 0]


def choose_func(func1, func2, assertion):
    x = 0
    for i in assertion:
        if i > 0:
            continue
        else:
            x = i
            break

    if x != 0:
        return func2(assertion)
    else:
        return func1(assertion)


number_line = input("Enter number using space:\n").split()

nums_list = [int(i) for i in number_line]
test = choose_func(square_nums, remove_negatives, nums_list)

print(test)

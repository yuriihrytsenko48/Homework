"""
Task 1

Write a function called oops that explicitly raises an IndexError exception when called. Then write another
function that calls oops inside a try/except statement to catch the error.
"""

test_list1 = [1, 2, 3, 4, 5, 6]
test_list2 = {1: 10, 2: 100, 3: 1000, 4: 10000, 5: 5000}


def oops(args, iterable_object):
    if args > 5:
        raise Exception("There are indexes from 0 to 5")
    else:
        return iterable_object[index]


def another_function(args, iterable_object):
    return oops(args, iterable_object)


while True:
    index = int(input("Enter index from 0 to 5.\n"))
    if index == "quit":
        break

    x = another_function(index, test_list1)
    y = another_function(index, test_list2)

    print(x)
    print(y)

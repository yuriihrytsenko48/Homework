
"""
Task 4

Створити лист із днями тижня.
В один рядок (ну або як завжди) створити словник виду: {1: “Monday”, 2:...
Також в один рядок або як вдасться створити зворотний словник {“Monday”: 1,
"""

days = ["Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"]

numbers = [1, 2, 3, 4, 5, 6, 7]

direct_dict = {number: day for number, day in zip(numbers, days)}
reverse_dict = {day: number for day, number in zip(days, numbers)}

print(direct_dict)
print(reverse_dict)

"""
Task 4

Custom exception

Create your custom exception named `CustomException`, you can inherit
from base Exception class, but extend its functionality to log every error
message to a file named `logs.txt`. Tips: Use __init__ method to extend
functionality for saving messages to file.
"""

import datetime


class CustomException(BaseException):

    def __init__(self, name_, message="Age is not accepted for work"):
        date = str(datetime.datetime.now()).split(".")[0]
        log = f"{date:<20}  {name:<20}  {message:>20}"

        self._log_writing(log)

        super().__init__(log)

    def _log_writing(self, log: str):
        with open("logs.txt", "a") as source_file:
            source_file.write(log)


while True:

    try:
        name = input("Enter your name:\t").strip().title()
        age = int(input("Enter your age:\t").strip())

        if age < 18:
            raise CustomException(name)
    except ValueError:
        print("Invalid enter!")

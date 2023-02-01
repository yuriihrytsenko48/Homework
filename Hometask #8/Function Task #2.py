"""Task 2

Creating a dictionary.

Create a function called make_country, which takes in a country’s name and capital
as parameters. Then create a dictionary from those two, with ‘name’ as a key and
‘capital’ as a parameter. Make the function print out the values of the
dictionary to make sure that it works as intended.
"""

country_capital_dict = {}


def make_country():
    while True:
        country = input("Enter country`s name\n")

        if country == "quit":
            for item in country_capital_dict.items():
                print(item)
            break

        capital = input("Enter name of the capital\n")

        if capital == "quit":
            for item in country_capital_dict.items():
                print(item)
            break

        country_capital_dict[country] = capital


make_country()

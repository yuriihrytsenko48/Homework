"""

Task 3

Product Store

Write a class Product that has three attributes:

- type
- name
- price

Then create a class ProductStore, which will have some Products and
will operate with all products in the store. All methods, in case they
can’t perform its action, should raise ValueError with appropriate error
information.

Tips: Use aggregation/composition concepts while implementing
the ProductStore class. You can also implement additional classes
to operate on a certain type of product, etc.

Also, the ProductStore class must have the following methods:

- add(product, amount) - adds a specified quantity of a single product
    with a predefined price premium for your store(30 percent)

- set_discount(identifier, percent, identifier_type= "name") - adds a
    discount for all products specified by input identifiers (type or name).
    The discount must be specified in percentage

- sell_product(product_name, amount) - removes a particular amount
    of products from the store if available, in other case raises an
    error. It also increments income if the sell_product method succeeds.

- get_income() - returns amount of many earned by ProductStore instance.

- get_all_products() - returns information about all available
    products in the store.

-get_product_info(product_name) - returns a tuple with product
    name and amount of items in the store.
"""


class Product:

    def __init__(self, product_type, name, price, amount):
        self.type = product_type
        self.name = name
        self.price = price
        self.discount = 1
        self.amount = amount

    def __str__(self):
        return self.name


class ProductStore:

    def __init__(self):
        self.products = {}
        self.bank = 0

    def product_adding(self):
        print("Ask the questions about product that you want to add!")
        characters = ["Name?", "Type?", "Price?", "Amount?"]
        characters2 = []

        for i in characters:
            i = input(i + "\n")
            characters2.append(i)

        product_name, product_type, product_price, product_amount = characters2
        product_name = Product(product_type, product_name, product_price, product_amount)
        self.products.update({f"{product_name}": product_name})

    def set_discount(self):
        product_name = input("product_name?\n").title().strip()
        product = self.products.get(product_name)
        product.discount = 1 - int(input("Set a discount: "))/100

    def sell_product(self):
        product_name = input("product_name?\n").title().strip()
        product = self.products.get(product_name)
        while True:
            selling_amount = int(input("Enter amount of product to sell: "))
            if product.amount >= selling_amount:
                product.amount -= selling_amount
                self.bank += (selling_amount * product.price * product.discount)
                break
            elif product.amount < selling_amount:
                print(f"Not enough product to sell! We have only {product.amount}!")
                continue

        if product.amount <= 0:
            del self.products[product_name]

    def get_income(self):
        print(f"The shop has {self.bank} income")

    def get_all_products(self):
        print(f"""{"Product name":<15}|{"Product type":<15}|{"Product price":<15}"""
              f"""|{"Product discount":<15}|{"Product amount":<15}""")
        for k in self.products.values():
            print(f"{k.name:<15}|{k.type:<15}|{k.price:<15}|{k.discount:<15}|{k.amount:<15}")

    def get_product_info(self):
        product_name = input("product_name?\n").title().strip()
        product = self.products.get(product_name)
        print(product.name, product.type, product.price, product.amount, product.discount)


name_list = ["Potato", "Tomato", "Banana", "Chocolate", "Pork"]
type_list = ["vegetable", "vegetable", "fruit", "sweets", "meat"]
price_list = [10, 25, 100, 70, 150]
amount_list = [100, 100, 100, 100, 100]

product_list = []

for name_, type_, price_, amount_ in zip(name_list, type_list, price_list, amount_list):
    name = Product(type_, name_, price_, amount_)
    product_list.append(name)

atb = ProductStore()

while product_list:
    x = product_list.pop()
    atb.products.update({f"{x}": x})

text = "\nEnter: \n" \
       "1 - to add product to shop.\n" \
       "2 - to set discount of product\n" \
       "3 - to sell product\n" \
       "4 - to see income of shop\n" \
       "5 - to get info about all products\n" \
       "quit - to end shopping\n" \
       "Use only numbers from 1 to 5.\n"

while True:
    atb.get_all_products()
    var = input(text).strip().lower()

    if var == "quit":
        break

    if not var.isnumeric():
        print("Use only numbers!")
        continue

    if var == "1":
        atb.product_adding()
    elif var == "2":
        atb.set_discount()
    elif var == "3":
        atb.sell_product()
    elif var == "4":
        atb.get_income()
    elif var == "5":
        atb.get_product_info()
    else:
        print("Invalid enter! Use numbers from 1 to 5!")
        continue

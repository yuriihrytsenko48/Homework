class Item:
    def __init__(self, name):
        self.name = name


class Box:

    def __init__(self, name, contain):
        self.name = name
        self.contain = contain

    def receiving_content(self, item):
        self.contain.append(item)

    def transmitting_content(self):
        return self.contain.pop()

    def contain_repr(self):
        for item in self.contain:
            print(item.name)


class Person:

    def __init__(self,
                 name,
                 age,
                 sex,
                 items):
        self.name = name
        self.age = age
        self.sex = sex
        self.items = items
        self.info = [self.name, self.age, self.sex]

    def receiving_item(self, item):
        self.items.append(item)

    def giving_item(self, person, item):
        person.receiving_item(item)

    def info_represent(self):
        for char in self.info:
            print(char)

    def items_represent(self):
        for item in self.items:
            print(item.name)


candy_1 = Item("Chocolate candy")
candy_2 = Item("Chocolate candy")
candy_3 = Item("Chocolate candy")
candy_4 = Item("Chocolate candy")
candy_5 = Item("Chocolate candy")
soda = Item("Soda")
bag = Item("Bag")
watch = Item("watch")

chocolate_box = Box("Chocolate candies box", [candy_1, candy_2, candy_3, candy_4])

forest = Person("Forest Gump", 35, "Man", [soda, chocolate_box, candy_5])
woman = Person("Woman", 60, "Women", [bag])
man = Person("Man", 50, "Man", [watch])

forest.info_represent()
print("\n")
forest.items_represent()
print("\n")
chocolate_box.contain_repr()
print("\n")

# Cause #1
forest.giving_item(woman, chocolate_box.transmitting_content())
forest.items_represent()
print("\n")
woman.items_represent()
print("\n")
chocolate_box.contain_repr()

# # Cause #2
# forest.giving_item(woman, candy_5)
# forest.items_represent()
# print("\n")
# woman.items_represent()

# Instead of write:
# item1 = Item("Phone")
# item1.name = "Phone"
# item1.price = 1000
# item1.quantity = 50
#
# item2 = Item("laptop")
# item2.name = "Laptop"
# item2.price = 1000
# item2.quantity = 50
#
# We can use __init__ function

class Item:
    pay_rate = 0.8  # To access this class attribute, use Item.pay_rate
    all = []
    def __init__(self, name: str, price: float, quantity=0):  # We can specifics the default data type
        # Run validation to received argument
        assert price >= 0, "Price must be non-negative"
        assert quantity >= 0, "quantity must be non-negative"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute: Stored all instance that made
        Item.all.append(self)

    def __repr__(self):     # Magic method to represent the object
        return f"Item({self.name}, {self.price},{self.quantity})"

    def calculate_price(self):
        return self.price * self.quantity

    def apply_disc(self):
        self.price = self.price * self.pay_rate
        self.price = self.price * self.pay_rate


item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

print(Item.all)

# print(len(Item.all))
# for item in Item.all:
#     print(f"{item.name}")
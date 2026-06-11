class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return '{} x{} | ${} each | Subtotal: ${}'.format(
            self.name, self.quantity,
            self.price, self.quantity * self.price
        )

    def sub_total(self):
        return self.price * self.quantity


class ShoppingCart:
    store_name = "JayanMart"

    def __init__(self, owner):
        self.owner = owner
        self.items = {}

    def get_total(self):
        total = 0
        for item in self.items.values():
            total += item.sub_total() 
        return round(total, 2)

    def __repr__(self):
        return '{}s cart | Items: {} | Total: ${}'.format(
            self.owner,
            len(self.items),
            self.get_total() 
        )

    def add_item(self, name, price, quantity):
        if name in self.items:
            self.items[name].quantity += quantity
        else:
            self.items[name] = Item(name, price, quantity)

    def __len__(self):
        return len(self.items)

    def __contains__(self, name):
        return name in self.items

    def __iter__(self):
        return iter(self.items.values())

    def __add__(self, other):
        merged = ShoppingCart(f"{self.owner} + {other.owner}")  
        for item in self.items.values():
            merged.add_item(item.name, item.price, item.quantity)
        for item in other.items.values():
            merged.add_item(item.name, item.price, item.quantity)
        return merged

    def __gt__(self, other):
        return self.get_total() > other.get_total()

    def __eq__(self, other):
        return self.get_total() == other.get_total() 


class PremiumCart(ShoppingCart):
    def __init__(self, owner, discount):
        super().__init__(owner)
        self.discount = discount

    def get_total(self):
        return round(super().get_total() * (1 - self.discount), 2)  

    def __repr__(self):
        return '{}s cart | Items: {} | Total: ${} | {}% discount applied'.format(
            self.owner,
            len(self.items),
            self.get_total(),
            int(self.discount * 100)
        )
    
cart1 = ShoppingCart("Jayan")
cart2 = ShoppingCart("Alex")

cart1.add_item("Apple", 1.99, 3)
cart1.add_item("Bread", 2.49, 1)
cart1.add_item("Milk", 3.99, 2)

cart2.add_item("Chips", 1.49, 5)

print(cart1)
print(len(cart1))
print(cart1 + cart2)
print(cart1 > cart2)
print(cart1 == cart2)
print("Apple" in cart1)
for item in cart1:
    print(item)

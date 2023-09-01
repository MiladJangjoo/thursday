class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item_name, qty):
        item = (item_name, qty)
        self.items.append(item)

    def remove_item(self, item_name):
        for item in self.items:
            if item[0] == item_name:
                self.items.remove(item)
                break

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item[1]
        return total
    
cart = ShoppingCart()
cart.add_item("banana", 2)
cart.add_item("milk", 6)
cart.add_item("egg", 1)
for item in cart.items:
    print(item[0], "  ", item[1])
cart.remove_item("egg")
for item in cart.items:
    print("new cart")
    print(item[0], "  ", item[1])
        
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self,name,price,quantity):
        self.items.append({"name":name,"price":price,"quantity":quantity})

    def remove_item(self,name):
        self.items = [item for item in self.items if item["name"] != name]
            
    def get_total(self):
        total = 0
        for item in self.items:
            total += item["price"]*item["quantity"]
        return f"Total: ${total}"
    
    def __str__(self):
        result = "Shopping Cart:\n"
        for item in self.items:
            result += f"- {item['name']} x{item['quantity']} @ ${item['price']:.2f} = ${item['price'] * item['quantity']: .2f}"

        return result.strip()

    def __len__(self):
        return len(self.items)
    

cart = ShoppingCart()
cart.add_item("Apple",2.5,3)
cart.add_item("Banana",1.2,5)
cart.remove_item("Banana")
print(cart)
print(f"Total: ${cart.get_total()}")
print(f"Items: {len(cart)}")


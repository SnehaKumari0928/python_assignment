
class Product:
    def __init__(self,product_id,name,price,quantity):
        self.product_id = product_id
        self.name = name
        if price > 0:
          self.price = price
        else:
           print("Price must be greater than 0.")
           return
        
        if quantity >= 0:
           self.quantity = quantity

        else:
           print("Quantity must be greater than 0")
           return
        
    def increase_stock(self,amount):
           self.quantity += amount

    def decrease_stock(self,amount):
           if self.quantity - amount <= 0:
               raise ValueError
           self.quantity -= amount

    def inventory_value(self):
           return self.price * self.quantity
    
    def is_in_stock(self):
           return self.quantity == 0
    
    def __str__(self):
           result = "Product Info: "
           result += f"Product Name: {self.name}, ProductId: {self.product_id}, Product Quantity: {self.quantity}"
           return result
                

class Inventory:
     def __init__(self):
          self.products = {}

     def add_product(self,product):
          product_keys = self.products.keys()

          if product.product_id not in product_keys:
               self.products[product.product_id] = product
               return
          print("Cannot add Duplicate IDs")

     def remove_product(self,product_id):
          product_keys = self.products.keys()

          if product_id not in product_keys:
               raise KeyError
          
          self.products.pop(product_id)

     def get_product(self,product_id):
          product = [value for id,value in self.products.items() if id == product_id]

          return product
     
     def total_inventory_value(self):
          total = 0
     
          for key,value in self.products.items():
               print(value)
               total += value.price * value.quantity

          print(total)

     def process_order(self,order_item):
          product_key = self.products.keys()
          
          for key,value in order_item.items():
              if key not in product_key:
                   raise KeyError
              if  self.products[key]["quantity"] - order_item[key] < 0:
                   raise ValueError
          total = 0
          for key,value in order_item.items():
               self.products[key]["quantity"] -= value
               total += self.products[key]["price"] * self.products[key]["quantity"]

          return total


p= Product("P1","Keyboard",1200,10)
p.decrease_stock(3) 
print(p.inventory_value())
print(p)

i = Inventory()
i.add_product(p)
i.remove_product("P1")
i.add_product(p)

print(i.get_product("P1"))
print(i.products)
print(i.total_inventory_value())
print(p)


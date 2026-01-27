class ShoppingCart:
    cart = []

    def add_item(self,name,price,quantity):
        ShoppingCart.cart.append({"name":name,"price":price,"quantity":quantity})

    def remove_item(self,name):
        for item in ShoppingCart.cart:
            if item["name"] == name:
                ShoppingCart.cart.remove(item)
            
    def get_total(self):
        total = 0
        for item in ShoppingCart.cart:
            total += item[self.__price]
        return f"Total: ${total}"
    
    def __str__(self):
        return f"{ShoppingCart.cart}"

    def __len__(self):
        s = []
        for item in ShoppingCart.cart:
            if item["name"] not in s:
                s.append(item)
        return len(s)
    

c = ShoppingCart()
c.add_item("Apple",2.5,3)
c.add_item("Banana",1.2,5)
c.remove_item("Banana")
print(c)
print(len(c))


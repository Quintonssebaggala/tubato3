class ShoppingCart(object):
    def __init__(self):
        self.total = 0
        self.items = {}

    def add_item(self, item_name, quantity, price):
        if item_name not in self.items:
            self.total += (quantity * price)
            self.items[item_name] = quantity
        else:
            self.items[item_name] += quantity
            self.total += (quantity * price)

    def remove_item(self, item_name, quantity, price):
        if item_name in self.items:
            if quantity >= self.items[item_name]:
                self.total -= (self.items[item_name] * price)
                del self.items[item_name]
            else:
                self.items[item_name] = self.items[item_name] - quantity
                self.total -= (quantity * price)

    def checkout(self, cash_paid):
        if cash_paid - self.total < 0:
            return "Cash paid not enough"
        else:
            return cash_paid - self.total


class Shop(ShoppingCart):
    def __init__(self):
        ShoppingCart.__init__(self)
        self.quantity = 100

    def remove_item(self):
        self.quantity -= 1
 
if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_item("MacBook",100,450)
    cart.add_item("MacAir",600,650)
    cart.add_item("HP",140,200)
    cart.add_item("Acer",80,320)
 
    #show all items
    print("All items: ",cart.items)
    #show total
    print("current Total:",cart.total)
 
    #remove macbook
    cart.remove_item("MacBook",90,450)
 
    print()
    #show all items
    print("after removing Macbook,120,450:",cart.items)
    print("Total after removing:",cart.total)
 
    print()
    print("after payment of 200")
    print(cart.checkout(5000))
 
    print()
    #instance of shop
    shop = Shop()
    shop.remove_item()
    print("Quantity in shop:",shop.quantity)
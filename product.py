class Product:
    def __init__(self, product_id, title, price, quantity):
        self.product_id = product_id
        self.title = title
        self.price = price
        self.quantity = quantity
    def apply_discount(self, percentage):
        if percentage < 0 or percentage > 100:
            return f"invalid discount"
        else:
            self.price = self.price - (self.price *(percentage / 100))
            return f"discount applied"
    def get_inventory_value(self):
        return float(f"{self.price * self.quantity}")

p = Product("P101", "Wireless Mouse", 1000.5, 5)
print(p.apply_discount(20))
print(p.price)
print(p.get_inventory_value())
print(p.apply_discount(150))
    

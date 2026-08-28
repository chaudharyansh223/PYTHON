product_prices = {
    "Laptop": 65000,
    "Keyboard": 1500,
    "Monitor": 18000,
    "Mouse": 600,
    "Headphones": 3200
}
products = {}
max_product = max(product_prices.items(),key=lambda x: x[1])
min_product = min(product_prices.items(),key=lambda x: x[1])
products.update({"max_product": max_product})
products.update({"min_product": min_product})
print(products)
        



PRODUCTS_FILE = "products.txt"
ORDERS_FILE = "orders.txt"

def load_products():
    try:
        with open(PRODUCTS_FILE, "r") as file:
            return [line.strip().split(",") for line in file.readlines()]
    except FileNotFoundError:
        return []

def save_products(products):
    with open(PRODUCTS_FILE, "w") as file:
        for product, price in products:
            file.write(f"{product},{price}\n")

def load_orders():
    try:
        with open(ORDERS_FILE, "r") as file:
            return [line.strip().split(",") for line in file.readlines()]
    except FileNotFoundError:
        return []

def save_orders(order):
    with open(ORDERS_FILE, "a") as file:
        for product, qty in order.items():
            file.write(f"{product},{qty}\n")

PRODUCTS_FILE = "products.txt"
ORDERS_FILE = "orders.txt"

def load_products():
    try:
        with open(PRODUCTS_FILE, "r") as file:
            products = []
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 2:  # If stock value is missing, set default stock to 10
                    product, price = parts
                    stock = "10"
                elif len(parts) == 3:
                    product, price, stock = parts
                else:
                    continue  # Ignore malformed lines
                products.append((product, float(price), int(stock)))
            return products
    except FileNotFoundError:
        return []

def save_products(products):
    with open(PRODUCTS_FILE, "w") as file:
        for product, price, stock in products:
            file.write(f"{product},{price},{stock}\n")

def load_orders():
    """Load orders from file and return as a formatted list."""
    try:
        with open(ORDERS_FILE, "r") as file:
            orders = [line.strip() for line in file.readlines()]
        return orders
    except FileNotFoundError:
        return []

def save_orders(name, order):
    """Save orders in a structured format."""
    with open(ORDERS_FILE, "a") as file:
        for product, qty in order.items():
            file.write(f"{name},{product},{qty}\n")

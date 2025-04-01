import json

PRODUCTS_FILE = "products.json"
ORDERS_FILE = "orders.json"

def load_products():
    try:
        with open(PRODUCTS_FILE, "r") as file:
            products = json.load(file)
            # Ensure each product has an 'image' key
            for product in products:
                if "image" not in product:
                    product["image"] = None  # Default if no image
            return products
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_products(products):
    with open(PRODUCTS_FILE, "w") as file:
        json.dump(products, file, indent=4)

def load_orders():
    try:
        with open(ORDERS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_orders(name, order):
    orders = load_orders()

    if not isinstance(orders, dict):
        orders = {}

    if name not in orders:
        orders[name] = {}

    for product, qty in order.items():
        if product in orders[name]:
            orders[name][product] += qty
        else:
            orders[name][product] = qty

    with open(ORDERS_FILE, "w") as file:
        json.dump(orders, file, indent=4)

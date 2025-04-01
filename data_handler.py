import json

# Define file paths for storing product and order data
PRODUCTS_FILE = "products.json"
ORDERS_FILE = "orders.json"

# Function to load products from the JSON file
def load_products():
    try:
        with open(PRODUCTS_FILE, "r") as file:
            products = json.load(file)  # Load product data from JSON
            
            # Ensure each product has an 'image' key, if missing assign None
            for product in products:
                if "image" not in product:
                    product["image"] = None  # Default if no image is provided
                    
            return products  # Return the list of products
    except (FileNotFoundError, json.JSONDecodeError):
        return []  # Return an empty list if file is missing or invalid JSON

# Function to save product data to the JSON file
def save_products(products):
    with open(PRODUCTS_FILE, "w") as file:
        json.dump(products, file, indent=4)  # Save products with indentation for readability

# Function to load orders from the JSON file
def load_orders():
    try:
        with open(ORDERS_FILE, "r") as file:
            return json.load(file)  # Load order data from JSON
    except (FileNotFoundError, json.JSONDecodeError):
        return []  # Return an empty list if file is missing or invalid JSON

# Function to save customer orders to the JSON file
def save_orders(name, order):
    orders = load_orders()  # Load existing orders

    # Ensure orders data structure is a dictionary
    if not isinstance(orders, dict):
        orders = {}

    # If the customer does not have an existing order, create an entry
    if name not in orders:
        orders[name] = {}

    # Update the customer's order details
    for product, qty in order.items():
        if product in orders[name]:
            orders[name][product] += qty  # Add to existing quantity
        else:
            orders[name][product] = qty  # Create a new entry for the product

    # Save the updated order data back to the file
    with open(ORDERS_FILE, "w") as file:
        json.dump(orders, file, indent=4)  # Save orders with indentation for readability

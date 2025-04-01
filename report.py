from datetime import datetime

# Function to generate a sales report
def generate_report(orders, products):
    report_date = datetime.now().strftime("%Y-%m-%d")  # Get the current date for the report

    total_orders = 0  # Initialize total orders count
    total_revenue = 0  # Initialize total revenue count
    product_sales = {}  # Dictionary to store product-wise sales data

    # Convert product list/dictionary to a proper format
    if isinstance(products, list):
        product_prices = {p["name"]: p["price"] for p in products}  # Extract name-price mapping from list
    elif isinstance(products, dict): 
        product_prices = {name: data["price"] for name, data in products.items()}  # Extract name-price mapping from dictionary
    else:
        product_prices = {}  # Default empty dictionary if format is incorrect

    # Loop through each customer order
    for customer, items in orders.items():
        order_total = 0  # Initialize total amount for the current order

        for product, qty in items.items():
            if product not in product_prices:
                print(f"Warning: Product '{product}' not found in product_prices dictionary.")
                continue  # Skip this product if not found
            
            price = product_prices[product]  # Get product price
            amount = qty * price  # Calculate total amount for the product
            order_total += amount  # Add to order total
            total_orders += qty  # Count total products sold

            # Accumulate total quantity and sales per product
            if product not in product_sales:
                product_sales[product] = {"quantity_sold": qty, "total_sales": amount}
            else:
                product_sales[product]["quantity_sold"] += qty
                product_sales[product]["total_sales"] += amount

        total_revenue += order_total  # Add order total to overall revenue

    # Prepare final report data
    report_data = {
        "date": report_date,
        "total_orders": total_orders,
        "total_revenue": total_revenue,
        "product_sales": product_sales  # Tracks both quantity and sales
    }

    return report_data  # Return the generated report
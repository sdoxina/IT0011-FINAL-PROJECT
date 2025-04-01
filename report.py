from datetime import datetime

def generate_report(orders, products):
    report_date = datetime.now().strftime("%Y-%m-%d")

    total_orders = 0
    total_revenue = 0
    product_sales = {}

    # Convert product list/dictionary to proper format
    if isinstance(products, list):
        product_prices = {p["name"]: p["price"] for p in products}
    elif isinstance(products, dict): 
        product_prices = {name: data["price"] for name, data in products.items()}
    else:
        product_prices = {}

    for customer, items in orders.items():
        order_total = 0

        for product, qty in items.items():
            if product not in product_prices:
                print(f"Warning: Product '{product}' not found in product_prices dictionary.")
                continue  # Skip this product if not found
            
            price = product_prices[product]
            amount = qty * price
            order_total += amount
            total_orders += qty  # Count total products sold

            # Accumulate total quantity and sales per product
            if product not in product_sales:
                product_sales[product] = {"quantity_sold": qty, "total_sales": amount}
            else:
                product_sales[product]["quantity_sold"] += qty
                product_sales[product]["total_sales"] += amount

        total_revenue += order_total

    report_data = {
        "date": report_date,
        "total_orders": total_orders,
        "total_revenue": total_revenue,
        "product_sales": product_sales  # Now correctly tracks both quantity and sales
    }

    return report_data

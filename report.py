from datetime import datetime

def generate_report(orders, products):
    report_date = datetime.now().strftime("%Y-%m-%d")

    total_orders = 0
    total_revenue = 0
    product_sales = {}

    # Convert products list to dictionary for fast lookup
    product_prices = {p["name"]: p["price"] for p in products} if isinstance(products, list) else products

    for customer, items in orders.items():
        order_total = 0

        for product, qty in items.items():
            price = product_prices.get(product, 0)  # Fetch price safely
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

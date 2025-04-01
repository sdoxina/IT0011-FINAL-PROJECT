# report_generator.py
from datetime import datetime

def generate_report(orders, products):
    report_date = datetime.now().strftime("%Y-%m-%d")
    total_orders = 0
    total_revenue = 0
    product_sales = {}

    for customer, items in orders.items():
        total_orders += 1
        order_total = 0

        for product, qty in items.items():
            if product != "order_date":
                price = next((p["price"] for p in products if p["name"] == product), 0)
                amount = qty * price
                order_total += amount

                if product not in product_sales:
                    product_sales[product] = qty
                else:
                    product_sales[product] += qty

        total_revenue += order_total

    report_data = {
        "date": report_date,
        "total_orders": total_orders,
        "total_revenue": total_revenue,
        "product_sales": product_sales
    }
    
    return report_data

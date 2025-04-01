import os
from datetime import datetime

# Function to generate a receipt
def generate_receipt(customer_name, order, receipt_no):
    total_amount = 0  # Variable to store the total amount
    receipt_content = (
        "============================================================\n"
        "                    Blumee Skincare Shop\n"
        "                 Padre Paredes St, Sampaloc,\n"
        "                  Manila, 1015 Metro Manila\n"
        "============================================================\n\n"
        "QTY   DESC                                AMT (PHP)\n"
        "------------------------------------------------------------\n"
    )
    
    # Loop through the order dictionary to generate order details
    for product, details in order.items():
        qty = details['qty']  # Quantity of the product
        price = details['price']  # Price per unit
        amount = qty * price  # Calculate total price for the product
        total_amount += amount  # Add to total amount
        receipt_content += f"{qty:<5} {product:<33} {amount:>8.2f}\n"

    # Append total amount and customer details to receipt content
    receipt_content += (
        "\n\n============================================================\n"
        f"TOTAL:                                    PHP {total_amount:.2f}\n"
        "============================================================\n\n"
        f"Customer: {customer_name:<30} Receipt #: {receipt_no}\n\n"
        f"Date: {datetime.now().strftime('%Y-%m-%d')}\n"
        "------------------------------------------------------------\n\n"
        "      Thank you for shopping with Blumee Skincare Shop!\n"
        "               We hope to see you again soon.\n\n"
        "           FOR COMPLAINTS, CALL: 0927-676-5377\n"
        "------------------------------------------------------------\n"
    )

    # Ensure the receipts folder exists
    receipts_folder = "receipts"
    os.makedirs(receipts_folder, exist_ok=True)

    # Save receipt to a text file in the receipts folder
    receipt_filename = os.path.join(receipts_folder, f"receipt_{receipt_no}.txt")
    with open(receipt_filename, "w") as file:
        file.write(receipt_content)
    
    return receipt_filename  # Return the filename of the generated receipt
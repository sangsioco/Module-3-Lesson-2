orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    # More orders...
]

def print_order_details(orders):
    for customer, product, quantity in orders:
        print(f"Customer: {customer}, Product: {product}, Quantity: {quantity}")

print_order_details(orders)

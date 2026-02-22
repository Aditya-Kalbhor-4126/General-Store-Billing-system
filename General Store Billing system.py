print("======== ALL IN ONE GENERAL STORE ========")
print("------------------------------------------")
customer_name = input("Enter customer name: ")
print("\n------------------ ITEMS -----------------")

basket = []
grand_total = 0

while True:
    item_name = input("Enter the item name: ")
    item_quantity = int(input("Enter the quantity: "))
    product_price = int(input("Enter the price: "))

    final_price = item_quantity * product_price

    print("------------------------------------------")
    print(f"Final price: {final_price}")
    print("------------------------------------------")

    # add to grand total
    grand_total += final_price

    # store item in basket
    basket.append({
        "name": item_name,
        "quantity": item_quantity,
        "price": product_price,
        "total": final_price
    })

    choice = input("Do you want to add more item (y/n): ")

    if choice.lower() != 'y':
        break

print("\n================= BILL ===================")

for item in basket:
    print(f"{item['name']} x {item['quantity']} = ₹{item['total']}")

print("------------------------------------------")
print("Customer name:", customer_name)
print("Grand Total : ₹",grand_total)
print("------------------------------------------")

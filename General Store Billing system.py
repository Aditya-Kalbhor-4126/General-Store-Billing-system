print("         ALL IN ONE GENERAL STORE ")
print("------------------------------------------")
customer_name = input("Enter customer name: ")
print("\n------------------ ITEMS -----------------")

import datetime
now = datetime.datetime.now()

basket = []
grand_total = 0
total_items = 0
while True:
    item_name = input("Enter the item name: ")
    item_quantity = int(input("Enter the quantity: "))
    product_price = int(input("Enter the price: "))

    final_price = item_quantity * product_price

    print(f"Final price: {final_price}")
    print("------------------------------------------")

    grand_total += final_price  # add to grand total
    total_items += item_quantity  # add to total items
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
print("\nTotal items purchased:",total_items)

print("------------------------------------------")
print("Customer name:", customer_name)
print("Date:",now.strftime("%d-%m-%Y"))
print("Time:",now.strftime("%H:%M:%S"))
gst = grand_total * 0.18
final_amount = grand_total + gst
print("Subtotal: ₹",grand_total)
print("------------------------------------------")
print("Total Amount (Incl. GST): ₹",final_amount)
print("------------------------------------------")

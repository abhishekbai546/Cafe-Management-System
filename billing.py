from datetime import datetime
from menu import MENU

def calculate_bill(cart):
    total = 0

    for x in cart:
        total += MENU[x["item"]] * x["qty"]

    gst = total * 0.05

    discount = 0

    if total > 500:
        discount = total * 0.10

    final = total + gst - discount

    return total, gst, discount, final

def save_order(name, phone, cart, total, gst, discount, final):
    with open("order_history.txt", "a", encoding="utf-8") as file:
        file.write("\n")
        file.write("=" * 50 + "\n")
        file.write("Date: " + str(datetime.now()) + "\n")
        file.write("Customer: " + name + "\n")
        file.write("Phone: " + phone + "\n")

        for x in cart:
            file.write(x["item"] + " x " + str(x["qty"]) + "\n")

        file.write("Subtotal: Rs" + str(total) + "\n")
        file.write("GST: Rs" + str(gst) + "\n")
        file.write("Discount: Rs" + str(discount) + "\n")
        file.write("Final Bill: Rs" + str(final) + "\n")

    with open("orders.txt", "a") as file:
        file.write(str(final) + "\n")

def generate_bill(name, phone, cart):
    if not cart:
        print("Cart is empty.")
        return

    total, gst, discount, final = calculate_bill(cart)

    print("\n========== BILL ==========")
    print("Customer:", name)
    print("Phone:", phone)

    for x in cart:
        amount = MENU[x["item"]] * x["qty"]
        print(x["item"], "x", x["qty"], "= Rs", amount)

    print("-------------------------")
    print("Subtotal :", total)
    print("GST      :", gst)
    print("Discount :", discount)
    print("Final    :", final)

    save_order(name, phone, cart, total, gst, discount, final)

    print("Order saved.")

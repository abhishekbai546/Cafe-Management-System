import os
from datetime import datetime

MENU = {
    "White Sauce Pasta": 180,
    "French Fries": 80,
    "KitKat Shake": 150,
    "Dosa": 60,
    "Idli": 50,
    "Pani Puri": 40,
    "Garlic Bread": 90,
    "Paneer Momos": 120,
    "Croissant": 100,
    "Chole Bhature": 100,
    "Choco Lava Cake": 80,
    "Brownie": 120,
    "Cold Coffee": 120,
    "Strawberry Shake": 130,
    "Banana Shake": 120,
    "Coffee": 80,
    "Tea": 40,
    "Sandwich": 120,
    "Burger": 150,
    "Pizza": 250
}

STOCK = {item: 50 for item in MENU}

orders_today = []


def pause():
    input("\nPress Enter to continue...")


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def login():
    print("=" * 40)
    print("CAFE MANAGEMENT SYSTEM LOGIN")
    print("=" * 40)

    while True:
        username = input("Username: ")
        password = input("Password: ")

        if username == "admin" and password == "1234":
            print("Login successful!")
            break
        else:
            print("Invalid credentials. Try again.")


def show_menu():
    print("\n------ MENU ------")
    for i, (item, price) in enumerate(MENU.items(), start=1):
        print(f"{i}. {item:<20} Rs{price}")
    print("-" * 30)


def show_stock():
    print("\n------ STOCK ------")
    for item, qty in STOCK.items():
        print(f"{item:<20} {qty}")


def customer_details():
    name = input("Customer Name: ")
    phone = input("Phone Number: ")
    return name, phone


def add_to_cart(cart):
    show_menu()

    try:
        choice = int(input("Enter item number: "))

        menu_list = list(MENU.keys())

        if choice < 1 or choice > len(menu_list):
            print("Invalid item number.")
            return

        item = menu_list[choice - 1]

        qty = int(input("Quantity: "))

        if qty <= 0:
            print("Invalid quantity.")
            return

        if qty > STOCK[item]:
            print("Not enough stock.")
            return

        STOCK[item] -= qty

        found = False

        for x in cart:
            if x["item"] == item:
                x["qty"] += qty
                found = True
                break

        if not found:
            cart.append({"item": item, "qty": qty})

        print(item, "added to cart.")

    except ValueError:
        print("Please enter valid numbers.")


def remove_from_cart(cart):
    if not cart:
        print("Cart is empty.")
        return

    view_cart(cart)

    item = input("Enter item to remove: ")

    for x in cart:
        if x["item"] == item:
            STOCK[item] += x["qty"]
            cart.remove(x)
            print("Removed.")
            return

    print("Item not found in cart.")


def view_cart(cart):
    if not cart:
        print("Cart is empty.")
        return

    print("\n------ CART ------")

    total = 0

    for x in cart:
        amount = MENU[x["item"]] * x["qty"]
        total += amount

        print(
            x["item"],
            "x",
            x["qty"],
            "= Rs",
            amount
        )

    print("Subtotal = Rs", total)


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
            file.write(
                x["item"]
                + " x "
                + str(x["qty"])
                + "\n"
            )

        file.write("Subtotal: Rs" + str(total) + "\n")
        file.write("GST: Rs" + str(gst) + "\n")
        file.write("Discount: Rs" + str(discount) + "\n")
        file.write("Final Bill: Rs" + str(final) + "\n")

    orders_today.append(final)


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

        print(
            x["item"],
            "x",
            x["qty"],
            "= Rs",
            amount
        )

    print("-------------------------")
    print("Subtotal :", total)
    print("GST      :", gst)
    print("Discount :", discount)
    print("Final    :", final)

    save_order(
        name,
        phone,
        cart,
        total,
        gst,
        discount,
        final
    )

    print("Order saved.")


def view_order_history():
    try:
        with open("order_history.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("No history found.")


def sales_report():
    print("\n------ SALES REPORT ------")

    if not orders_today:
        print("No sales today.")
        return

    print("Orders:", len(orders_today))
    print("Revenue:", sum(orders_today))
    print("Average:", sum(orders_today) / len(orders_today))


def feedback():
    text = input("Enter feedback: ")

    with open("feedback.txt", "a") as file:
        file.write(
            str(datetime.now())
            + " : "
            + text
            + "\n"
        )

    print("Feedback saved.")


def restock():
    item = input("Item name: ")

    if item not in STOCK:
        print("Invalid item.")
        return

    qty = int(input("Add quantity: "))

    STOCK[item] += qty

    print("Stock updated.")


def search_item():
    word = input("Search item: ").lower()

    found = False

    for item, price in MENU.items():
        if word in item.lower():
            print(item, "-", price)
            found = True

    if not found:
        print("No matching item.")


def cafe_information():
    print("\nWelcome to Python Cafe")
    print("Open: 9 AM - 10 PM")
    print("GST: 5%")
    print("Discount: 10% above Rs500")


def customer_menu():
    name, phone = customer_details()

    cart = []

    while True:
        print("\nCUSTOMER MENU")
        print("1. Show Menu")
        print("2. Search Item")
        print("3. Add To Cart")
        print("4. Remove From Cart")
        print("5. View Cart")
        print("6. Generate Bill")
        print("7. Cafe Information")
        print("8. Back")

        choice = input("Choice: ")

        if choice == "1":
            show_menu()

        elif choice == "2":
            search_item()

        elif choice == "3":
            add_to_cart(cart)

        elif choice == "4":
            remove_from_cart(cart)

        elif choice == "5":
            view_cart(cart)

        elif choice == "6":
            generate_bill(name, phone, cart)
            cart.clear()

        elif choice == "7":
            cafe_information()

        elif choice == "8":
            break

        else:
            print("Invalid choice.")


def admin_menu():
    while True:
        print("\nADMIN MENU")
        print("1. View Stock")
        print("2. Restock Item")
        print("3. View Order History")
        print("4. Sales Report")
        print("5. Back")

        choice = input("Choice: ")

        if choice == "1":
            show_stock()

        elif choice == "2":
            restock()

        elif choice == "3":
            view_order_history()

        elif choice == "4":
            sales_report()

        elif choice == "5":
            break

        else:
            print("Invalid choice.")


def main():
    login()

    while True:
        print("\n===== MAIN MENU =====")
        print("1. Customer")
        print("2. Admin")
        print("3. Feedback")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            customer_menu()

        elif choice == "2":
            admin_menu()

        elif choice == "3":
            feedback()

        elif choice == "4":
            print("Thank you!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()

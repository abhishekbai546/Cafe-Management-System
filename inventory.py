from menu import MENU

STOCK = {item: 50 for item in MENU}

def show_stock():
    print("\n------ STOCK ------")

    for item, qty in STOCK.items():
        print(f"{item:<20} {qty}")

def restock():
    item = input("Item name: ")

    if item not in STOCK:
        print("Invalid item.")
        return

    qty = int(input("Add quantity: "))

    STOCK[item] += qty

    print("Stock updated.")

def view_order_history():
    try:
        with open("order_history.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("No history found.")

def sales_report():
    try:
        with open("orders.txt", "r") as file:
            orders = [float(line.strip()) for line in file]

        print("Orders:", len(orders))
        print("Revenue:", sum(orders))

        if orders:
            print("Average:", sum(orders) / len(orders))

    except FileNotFoundError:
        print("No sales today.")

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

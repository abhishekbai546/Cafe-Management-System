from menu import MENU, show_menu, search_item
from inventory import STOCK
from billing import generate_bill
from file_manager import cafe_information

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

        for x in cart:
            if x["item"] == item:
                x["qty"] += qty
                print(item, "added to cart.")
                return

        cart.append({"item": item, "qty": qty})

        print(item, "added to cart.")

    except ValueError:
        print("Please enter valid numbers.")

def remove_from_cart(cart):
    if not cart:
        print("Cart is empty.")
        return

    item = input("Enter item to remove: ")

    for x in cart:
        if x["item"] == item:
            STOCK[item] += x["qty"]
            cart.remove(x)
            print("Removed.")
            return

    print("Item not found.")

def view_cart(cart):
    if not cart:
        print("Cart is empty.")
        return

    total = 0

    for x in cart:
        amount = MENU[x["item"]] * x["qty"]
        total += amount
        print(x["item"], "x", x["qty"], "= Rs", amount)

    print("Subtotal = Rs", total)

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

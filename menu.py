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

def show_menu():
    print("\n------ MENU ------")

    for i, (item, price) in enumerate(MENU.items(), start=1):
        print(f"{i}. {item:<20} Rs{price}")

    print("-" * 30)

def search_item():
    word = input("Search item: ").lower()

    found = False

    for item, price in MENU.items():
        if word in item.lower():
            print(item, "-", price)
            found = True

    if not found:
        print("No matching item.")

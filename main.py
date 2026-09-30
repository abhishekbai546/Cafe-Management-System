from customer import customer_menu
from inventory import admin_menu
from file_manager import login, feedback

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

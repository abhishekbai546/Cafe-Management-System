import os
from datetime import datetime

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

def feedback():
    text = input("Enter feedback: ")

    with open("feedback.txt", "a") as file:
        file.write(str(datetime.now()) + " : " + text + "\n")

    print("Feedback saved.")

def cafe_information():
    print("\nWelcome to Python Cafe")
    print("Open: 9 AM - 10 PM")
    print("GST: 5%")
    print("Discount: 10% above Rs500")

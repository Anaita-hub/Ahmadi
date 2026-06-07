
#Mini Banking system with PIN and file storage
import os

FILE_NAME = "bank_data.txt"

def create_account():
    name = input("Enter your name: ")
    pin = input("Set a 4-digit PIN: ")
    balance = 0

    with open(FILE_NAME, "w") as file:
        file.write(f"{name}\n{pin}\n{balance}")

    print("Account created successfully!")

def login():
    if not os.path.exists(FILE_NAME):
        print("No account found. Please create an account first.")
        return False

    pin = input("Enter your PIN: ")

    with open(FILE_NAME, "r") as file:
        data = file.readlines()

    if pin == data[1].strip():
        print("Login successful!")
        return True
    else:
        print("Wrong PIN!")
        return False

def get_balance():
    with open(FILE_NAME, "r") as file:
        data = file.readlines()
    return float(data[2])

def update_balance(new_balance):
    with open(FILE_NAME, "r") as file:
        data = file.readlines()

    data[2] = str(new_balance)

    with open(FILE_NAME, "w") as file:
        file.writelines(data)

def show_menu():
    print("\n=== BANK MENU ===")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

while True:
    print("\n=== MINI BANKING SYSTEM ===")
    print("1. Create Account")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        create_account()

    elif choice == "2":
        if login():
            while True:
                show_menu()
                option = input("Enter option: ")

                if option == "1":
                    balance = get_balance()
                    print("Current Balance: ₹", balance)

                elif option == "2":
                    amount = float(input("Enter deposit amount: ₹"))
                    balance = get_balance()
                    balance += amount
                    update_balance(balance)
                    print("Deposit successful!")

                elif option == "3":
                    amount = float(input("Enter withdrawal amount: ₹"))
                    balance = get_balance()
                    if amount <= balance:
                        balance -= amount
                        update_balance(balance)
                        print("Withdrawal successful!")
                    else:
                        print("Insufficient balance.")

                elif option == "4":
                    print("Logged out successfully.")
                    break

                else:
                    print("Invalid option.")

    elif choice == "3":
        print("Thank you for using the banking system 👋")
        break

    else:
        print("Invalid choice.")

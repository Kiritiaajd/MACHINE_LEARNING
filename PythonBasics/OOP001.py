import csv
import os


class Atm:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.customers = self.load_customers(csv_file)
        self.current_customer = None
        self.max_attempts = 3
        self.log_in()

    def load_customers(self, csv_file):
        customers = {}
        with open(csv_file, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                customers[row['Account Number']] = {
                    'name': row['Name'],
                    'pin': row['PIN'],
                    'balance': float(row['Balance'])
                }
        return customers

    def save_customers(self):
        with open(self.csv_file, mode='w', newline='') as file:
            fieldnames = ['Name', 'Account Number', 'PIN', 'Balance']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for acc_no, details in self.customers.items():
                writer.writerow({
                    'Name': details['name'],
                    'Account Number': acc_no,
                    'PIN': details['pin'],
                    'Balance': details['balance']
                })

    def log_in(self):
        print("Hello! Welcome to Banking")
        attempts = 0
        while attempts < self.max_attempts:
            acc_no = input("Enter your account number: ")
            entered_pin = input("Enter your PIN: ")
            if acc_no in self.customers and self.customers[acc_no]['pin'] == entered_pin:
                self.current_customer = acc_no
                print(f"Welcome {self.customers[acc_no]['name']}")
                self.menu()
                break
            else:
                attempts += 1
                print(f"Invalid account number or PIN. Attempts remaining: {self.max_attempts - attempts}")
        if attempts == self.max_attempts:
            print("Too many failed attempts. Your session is locked.")

    def change_pin(self):
        old_pin = input("Enter your old PIN: ")
        if self.customers[self.current_customer]['pin'] == old_pin:
            new_pin = input("Enter your new PIN: ")
            confirm_pin = input("Confirm your new PIN: ")
            if new_pin == confirm_pin and new_pin.isdigit() and len(new_pin) == 4:
                self.customers[self.current_customer]['pin'] = new_pin
                print("PIN changed successfully!")
                self.save_customers()
            else:
                print("PIN change failed. Ensure your PIN is 4 digits long and matches the confirmation.")
        else:
            print("Incorrect old PIN")

    def withdraw(self):
        try:
            amount = float(input("Enter amount to withdraw: "))
            if amount > self.customers[self.current_customer]['balance']:
                print("Insufficient balance!")
            else:
                self.customers[self.current_customer]['balance'] -= amount
                print(
                    f"{amount} withdrawn successfully. Your new balance is {self.customers[self.current_customer]['balance']}.")
                self.save_customers()
        except ValueError:
            print("Invalid input. Please enter a numeric amount.")

    def check_balance(self):
        print(f"Your current balance is {self.customers[self.current_customer]['balance']}.")

    def deposit(self):
        try:
            amount = float(input("Enter amount to deposit: "))
            self.customers[self.current_customer]['balance'] += amount
            print(
                f"{amount} deposited successfully. Your new balance is {self.customers[self.current_customer]['balance']}.")
            self.save_customers()
        except ValueError:
            print("Invalid input. Please enter a numeric amount.")

    def menu(self):
        while True:
            user_input = input('''\nHow would you like to proceed?
            Press:
            1 to Change PIN
            2 to Withdraw 
            3 to Check Balance 
            4 to Deposit
            5 to Logout
            ''')

            if user_input == "1":
                self.change_pin()
            elif user_input == "2":
                self.withdraw()
            elif user_input == "3":
                self.check_balance()
            elif user_input == "4":
                self.deposit()
            elif user_input == "5":
                print("Logging out. Thank you for using our services!")
                self.current_customer = None
                self.log_in()
                break
            else:
                print("Invalid option, please try again.")


# Example usage
csv_file = '/mnt/data/atm_customers.csv'
atm = Atm(csv_file)

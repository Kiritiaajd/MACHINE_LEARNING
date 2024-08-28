class Atm:
    def __init__(self):
        self.name = "Kiriti Aajad"
        self.acc_no = "12345"
        self.pin = ""
        self.balance = 0

        self.log_in()

    def log_in(self):
        print("Hello Welcome to Banking")
        acc_no = input("Enter  your account No :")
        if acc_no == self.acc_no:
            print("Welcome ", self.name)
        else:
            print("Invalid Acc No")
    @staticmethod
    def menu():
        user_input = input('''How would you like to proceed
        press :
        1 for change pin
        2 for Withdraw 
        3 for Check Balance 
        4 for deposit
        ''')

        if user_input == "1":
            print("Change pin : ")
        elif user_input == "2":
            print("Withdrawal")
        elif user_input == "3":
            print("Check Balance")
        elif user_input == "4":
            print("Deposit")
        else:
            print("Exit")


atm = Atm()

atm.acc_no = "1234"
atm.name = "Kiriti Aajad"
atm.pin = '9931'
atm.balance = 100000


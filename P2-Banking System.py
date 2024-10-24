class BankAccount:
    def __init__(self, username, password, balance=0):
        self.username = username
        self.password = password
        self.balance = balance

    def login(self, username, password):
        if self.username == username and self.password == password:
            print("Login successful!")
            return True
        else:
            print("Login failed! Incorrect username or password.")
            return False

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}. Current balance: {self.balance}")
        else:
            print("Enter a valid amount to deposit.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: {amount}. Current balance: {self.balance}")
        else:
            print("Insufficient balance or invalid amount.")

    def check_balance(self):
        print(f"Your current balance is: {self.balance}")


def banking_system():
    # Creating an account with initial login credentials
    account = BankAccount("user1", "pwd123", 1000)

    print("Welcome to the Banking System!")
    # Account Login
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if account.login(username, password):
        while True:
            print("\n1. Deposit Money")
            print("2. Withdraw Money")
            print("3. Check Balance")
            print("4. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
            elif choice == "2":
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)
            elif choice == "3":
                account.check_balance()
            elif choice == "4":
                print("Thank you for banking with us!")
                break
            else:
                print("Invalid choice, please try again.")

# Running the banking system
banking_system()

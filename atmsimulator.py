class ATM:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def check_balance(self):
        print(f"Your current balance is: ${self.balance:.2f}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Successfully deposited ${amount:.2f}")
        else:
            print("Invalid deposit amount. Please enter a positive number.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Successfully withdrew ${amount:.2f}")
            else:
                print("Insufficient balance.")
        else:
            print("Invalid withdraw amount. Please enter a positive number.")

def atm_menu():
    atm = ATM(initial_balance=100)  # Initialize ATM with an initial balance of 100
    while True:
        print("\nATM Simulator")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            atm.check_balance()
        elif choice == '2':
            amount = float(input("Enter the amount to deposit: "))
            atm.deposit(amount)
        elif choice == '3':
            amount = float(input("Enter the amount to withdraw: "))
            atm.withdraw(amount)
        elif choice == '4':
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    atm_menu()

class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        elif amount <= 0:
            return "Invalid withdrawal amount."
        else:
            return "Insufficient balance."

def main():
    atm = ATM()  # Create an ATM instance with an initial balance

    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Select an option (1/2/3/4): ")

        if choice == "1":
            balance = atm.check_balance()
            print(f"Current balance: ${balance}")

        elif choice == "2":
            deposit_amount = float(input("Enter the deposit amount: $"))
            result = atm.deposit(deposit_amount)
            print(result)

        elif choice == "3":
            withdrawal_amount = float(input("Enter the withdrawal amount: $"))
            result = atm.withdraw(withdrawal_amount)
            print(result)

        elif choice == "4":
            print("Thank you for using the ATM. Have a nice day!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
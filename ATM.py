class Account:
    def __init__(self, account_number, name, pin):
        self.account_number = account_number
        self.name = name
        self.pin = pin
        self.balance = 0
        self.transactions = []

    def check_pin(self, entered_pin):
        return self.pin == entered_pin

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")

        self.balance += amount
        self.transactions.append(f"Deposited ${amount}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")

        if amount > self.balance:
            raise ValueError("Insufficient balance.")

        self.balance -= amount
        self.transactions.append(f"Withdrew ${amount}")

    def show_transactions(self):
        return self.transactions


class ATM:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.account_number] = account

    def login(self, account_number, pin):
        if account_number not in self.accounts:
            raise ValueError("Account not found.")

        account = self.accounts[account_number]

        if not account.check_pin(pin):
            raise ValueError("Incorrect PIN.")

        return account


class ATMController:
    def __init__(self):
        self.atm = ATM()
        self.current_account = None

        # Creating multiple accounts
        self.atm.add_account(Account("1001", "Shaurya", "1234"))
        self.atm.add_account(Account("1002", "Kshitij", "5678"))
        self.atm.add_account(Account("1003", "Sapana", "1111"))

    def get_number(self, prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Please enter a valid number.")

    def login(self):
        print("\n===== SBI ATM LOGIN =====")

        while True:
            account_number = input("Enter account number: ")
            pin = input("Enter PIN: ")

            try:
                self.current_account = self.atm.login(
                    account_number,
                    pin
                )

                print(
                    f"\nLogin successful. "
                    f"Welcome {self.current_account.name}!"
                )

                break

            except ValueError as error:
                print(error)

    def display_menu(self):
        print("\n===== SBI ATM =====")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transaction History")
        print("5. Logout")
        print("6. Exit")

    def check_balance(self):
        balance = self.current_account.check_balance()

        print(f"Your current balance is: ${balance}")

    def deposit(self):
        while True:
            try:
                amount = self.get_number(
                    "Enter amount to deposit: "
                )

                self.current_account.deposit(amount)

                print(
                    f"Successfully deposited ${amount}"
                )

                break

            except ValueError as error:
                print(error)

    def withdraw(self):
        while True:
            try:
                amount = self.get_number(
                    "Enter amount to withdraw: "
                )

                self.current_account.withdraw(amount)

                print(
                    f"Successfully withdrew ${amount}"
                )

                break

            except ValueError as error:
                print(error)

    def transaction_history(self):
        transactions = (
            self.current_account.show_transactions()
        )

        print("\n===== TRANSACTION HISTORY =====")

        if len(transactions) == 0:
            print("No transactions found.")

        else:
            for number, transaction in enumerate(
                transactions,
                start=1
            ):
                print(f"{number}. {transaction}")

    def run(self):
        while True:

            if self.current_account is None:
                self.login()

            self.display_menu()

            choice = input(
                "Please choose an option: "
            )

            if choice == "1":
                self.check_balance()

            elif choice == "2":
                self.deposit()

            elif choice == "3":
                self.withdraw()

            elif choice == "4":
                self.transaction_history()

            elif choice == "5":
                print(
                    f"Goodbye "
                    f"{self.current_account.name}."
                )

                self.current_account = None

            elif choice == "6":
                print(
                    "Thank you for using SBI ATM."
                )
                break

            else:
                print(
                    "Invalid choice. Please try again."
                )


def main():
    controller = ATMController()
    controller.run()


if __name__ == "__main__":
    main()
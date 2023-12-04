class Account:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Can't withdraw negative or 0 amount")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds. Withdrawal denied.")


class SavingsAccount(Account):
    def __init__(self, account_number, account_holder, balance=0, interest_rate=0.02):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)
        print(f"Interest of ${interest} added. New balance: ${self.balance}")


class CheckingAccount(Account):
    def __init__(self, account_number, account_holder, balance=0, overdraft_limit=100):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit

    # overdraft_limit represents the maximum negative balance the account can reach

    def withdraw(self, amount):
        if amount <= (self.balance + self.overdraft_limit):
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Overdraft limit exceeded! You are broke!")


def main():
    savings_account = SavingsAccount("TEOG351293455", "Teo", balance=1000)
    savings_account.deposit(500)
    savings_account.withdraw(200)
    savings_account.calculate_interest()

    checking_account = CheckingAccount("TEOFATA332992", "Teodora", balance=500, overdraft_limit=200)
    checking_account.deposit(300)
    checking_account.withdraw(1000) #1001


if __name__ == "__main__":
    main()
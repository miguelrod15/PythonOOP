class BankAccount:
    """
    Creating a Bank Account which allows to make deposits and withdrawals.
    """
    def __init__(self, name, balance = 0):      # Constructor Method
        # Insantance Attributes
        self.name = name
        self.balance = balance
    
    def __str__(self):
        return f"{self.name}'s account has €{self.balance:,.2f}"
    
    # Methods
    
    def deposit(self, value):
        self.balance += value
        print(f"Deposit of €{value:,.2f} authorizied in the account")

    def withdrawals(self, value):
        if value > self.balance:
            print(f"Withdrawals denied of €{value:,.2f} in this account")
        else:
            self.balance -= value
            print(f"€{value:,.2f} were accepted for withdrawal from this account.")

# Object declaration

b1 = BankAccount("Miguel", 5000)
b1.deposit(500)
b1.withdrawals(1250)
print(b1)
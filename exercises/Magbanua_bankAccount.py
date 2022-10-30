class BankAccount:
    def __init__(self):
        """Class that represents a bank account

        Attributes:
            accNumber : The account number
            balance : The current balance of the bank account
            dateOpened : The date when the bank account was opened
        """
        self.accNumber = 1
        self.balance = 1515
        self.dateOpened = '10/27/1987'

    def deposit(self, dep):
        """Deposits an amount to the current balance.

        Args:
            dep : The amount to deposit.
        """
        self.balance = self.balance + dep
        print(self.balance)
    
    def withdraw(self, wd):
        """Withdraws certain amount from the current balance.

        Args:
            wd : The amount to withdraw.
        """
        self.balance = self.balance - wd
        print(self.balance)
    
    def drop(self, accNumber):
        """Sets the current balance to 0 if the account number specified is equal to the
        account number of this bank account.
        """
        if self.accNumber != accNumber:
            # invalid account number
            print('Invalid Transaction!')
            return
        
        # valid account therefore set balance to 0
        self.balance = 0
        print(self.balance)

# create the bank account
bankAccount = BankAccount()

# get the user inputs
user_input = input().split()

transaction = user_input[0]
account_number = int(user_input[1])
amount = int(user_input[2])

if transaction not in ['dep', 'wd', 'drop']:
    print('Invalid Transaction!')
elif transaction == 'drop':
    if amount != 0:
        print('Invalid Transaction!')
    else:
        bankAccount.drop(account_number)
elif transaction == 'dep':
    bankAccount.deposit(amount)
elif transaction == 'wd':
    bankAccount.withdraw(amount)

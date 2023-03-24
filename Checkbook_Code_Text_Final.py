import os
class Bank:
    def __init__(self):
        self.name = ''
        self.balance_file = 'balance.txt'
        self.load_balance()
    def welcome(self):
        self.name = input('Welcome to your terminal checkbook! Please enter your name: ')
    def print_current_balance(self):
        print('Your current balance is: {:.2f}'.format(self.total_amount))
    def deposit(self):
        amount = float(input('Hello {}, please enter the amount to deposit: '.format(self.name)))
        self.total_amount += amount
        self.save_balance()
        self.print_current_balance()
    def withdraw(self):
        amount = float(input('Hello {}, please enter the amount to withdraw: '.format(self.name)))
        if amount > self.total_amount:
            print('Insufficient balance!!')
        else:
            self.total_amount -= amount
            self.save_balance()
            self.print_current_balance()
    def load_balance(self):
        if os.path.isfile(self.balance_file):
            with open(self.balance_file, 'r') as f:
                self.total_amount = float(f.read().strip())
        else:
            self.total_amount = 0.00
    def save_balance(self):
        with open(self.balance_file, 'w') as f:
            f.write('{:.2f}'.format(self.total_amount))
if __name__ == "__main__":
    bank = Bank()
    bank.welcome()
    while True:
        input_value = int(input('What would you like to do?\n1. View your current balance\n2. Record a credit (deposit)\n3. Record a debit (withdraw)\n4. Exit\n'))
        if input_value == 1:
            bank.print_current_balance()
        elif input_value == 2:
            bank.deposit()
        elif input_value == 3:
            bank.withdraw()
        elif input_value == 4:
            print('Thank you for using your terminal checkbook!')
            break
        else:
            print('Invalid choice') 

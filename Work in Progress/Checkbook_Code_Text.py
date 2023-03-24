class Bank:
	def __init__(self):
		self.total_amount = 0.00
		self.name = ''

	def welcome(self):
		self.name = input('Welcome to your terminal checkbook! Please Enter your name : ')

	def print_current_balance(self):
		print('Your Current balance is: {}'.format(self.total_amount))
    
	with open('checkbook_file.txt', 'w') as f:
		f.write('print_current_balance')
    
	def deposit(self):
		self.total_amount += float(input('Hello {}, please enter amount to deposit : '.format(self.name)))
		self.print_current_balance()

	def withdraw(self):
		amount_to_withdraw = float(input('Enter amount to withdraw : '))

		if amount_to_withdraw > self.total_amount:
			print('Insufficient balance !!')
		else:
			self.total_amount -= amount_to_withdraw

		self.print_current_balance()


if __name__=="__main__":
	bank = Bank()
	bank.welcome()

	while True:
		input_value = int(input('What would you like to do?\n1 view your current balance\n2 record a credit (deposit)\n3 record a debit (withdraw)\n4 to exit'))

		if input_value == 1:
			bank.print_current_balance()
		elif input_value == 2:
			bank.deposit()
		elif input_value == 3:
			bank.withdraw()
		elif input_value == 4:
			print("Bye")
			break            
		else:
			print('Invalid choice')
Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class Account():
	def __init__(self,name,nbr,balance):
		self.name = name
		self.nbr = nbr
		self.balance = balance
	def __str__(self):
		return "{}'s account # {} current balance is {}".format(self.name,self.nbr,self.balance)
	def deposit(self,amount):
		self.balance += amount
		print("Deposit is successful. Current balance is {}".format(self.balance))
	def withdraw(self,amount):
		if amount > self.balance:
			print("Insufficient balance to make withdrwal")
		else:
			self.balance -= amount
			print("{} Rs has been withdrawn. Current balance is {}".format(amount,self.balance))

>>> class Checking(Account):
	def __init__(self,name,nbr,balance):
		super().__init__(name,nbr,balance)
	def __str__(self):
		return "{}'s account # {} Checking account balance is {}".format(self.name,self.nbr,self.balance)

>>> class Saving(Account):
	def __init__(self,name,nbr,balance):
		super().__init__(name,nbr,balance)
	def __str__(self):
		return "{}'s account # {} Savings account balance is {}".format(self.name,self.nbr,self.balance)

	
>>> class Business(Account):
	def __init__(self,name,nbr,balance):
		super().__init__(name,nbr,balance)
	def __str__(self):
		return "{}'s account # {} Business account balance is {}".format(self.name,self.nbr,self.balance)

	
>>> class Customer:
	def __init__(self,name,pin):
		self.name = name
		self.pin = pin
		self.accts = {'C':[],'S':[],'B':[]}
	def open_checking(self,name,nbr,balance):
		self.accts['C'].append(Checking(name,nbr,balance))
	def open_saving(self,name,nbr,balance):
		self.accts['S'].append(Saving(name,nbr,balance))
	def open_business(self,name,nbr,balance):
		self.accts['B'].append(Business(name,nbr,balance))
	def total_deposit(self):
		total = 0
		for acct in self.accts['C']:
			print(acct)
			total += acct.balance
		for acct in self.accts['S']:
			print(acct)
			total += acct.balance
		for acct in self.accts['B']:
			print(acct)
			total += acct.balance
		print('Total deposits: {}'.format(total))


>>> def make_dep(name,acct_type,nbr,amnt):
	for acct in name.accts[acct_type]:
		if acct.nbr == nbr:
			acct.deposit(amnt)

>>> def make_wtd(name,acct_type,nbr,amnt):
	for acct in name.accts[acct_type]:
		if acct.nbr == nbr:
			acct.withdraw(amnt)

			
>>> 
>>> Viki = Customer('Viki',1001)
>>> Viki.open_checking('Viki',949614,5000.00)
>>> Viki.open_saving('Viki',742844,4000.00)
>>> Viki.open_business('Viki',949742,4500.00)
>>> Viki.total_deposit()
Viki's account # 949614 Checking account balance is 5000.0
Viki's account # 742844 Savings account balance is 4000.0
Viki's account # 949742 Business account balance is 4500.0
Total deposits: 13500.0
>>> Viki.open_checking('Viki',949615,5500.00)
>>> Viki.total_deposit()
Viki's account # 949614 Checking account balance is 5000.0
Viki's account # 949615 Checking account balance is 5500.0
Viki's account # 742844 Savings account balance is 4000.0
Viki's account # 949742 Business account balance is 4500.0
Total deposits: 19000.0
>>> Sri = Customer('Sri',2001)
>>> Sri.open_checking('Sri',109876,4500.00)
>>> Sri.open_checking('Sri',109873,4900.00)
>>> Sri.total_deposit()
Sri's account # 109876 Checking account balance is 4500.0
Sri's account # 109873 Checking account balance is 4900.0
Total deposits: 9400.0
>>> Viki.total_deposit()
Viki's account # 949614 Checking account balance is 5000.0
Viki's account # 949615 Checking account balance is 5500.0
Viki's account # 742844 Savings account balance is 4000.0
Viki's account # 949742 Business account balance is 4500.0
Total deposits: 19000.0
>>> Viki.accts['C']
[<__main__.Checking object at 0x044B2550>, <__main__.Checking object at 0x044B2670>]
>>> print(Viki.accts['C'])
[<__main__.Checking object at 0x044B2550>, <__main__.Checking object at 0x044B2670>]
>>> make_dep(Viki,'S',742844,9000.00)
Deposit is successful. Current balance is 13000.0
>>> make_dep(Viki,'B',984588,500.0)
>>> make_dep(Viki,'B',949742,9900.00)
Deposit is successful. Current balance is 14400.0
>>> Viki.total_deposit()
Viki's account # 949614 Checking account balance is 5000.0
Viki's account # 949615 Checking account balance is 5500.0
Viki's account # 742844 Savings account balance is 13000.0
Viki's account # 949742 Business account balance is 14400.0
Total deposits: 37900.0
>>> make_wtd(Viki,'B',949742,900.00)
900.0 Rs has been withdrawn. Current balance is 13500.0
>>> make_wtd(Viki,'B',949742,99900.00)
Insufficient balance to make withdrwal
>>> Viki.total_deposit()
Viki's account # 949614 Checking account balance is 5000.0
Viki's account # 949615 Checking account balance is 5500.0
Viki's account # 742844 Savings account balance is 13000.0
Viki's account # 949742 Business account balance is 13500.0
Total deposits: 37000.0
>>> 

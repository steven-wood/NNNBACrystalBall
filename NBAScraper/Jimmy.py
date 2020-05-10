class Jimmy:
	def __init__(self, initialAmt):
		self.balance = initialAmt

	def bet(self, amount, odds, outcome):
		odds = int(odds)
		outcome = int(outcome)
		if outcome == 0:
			self.decreaseBalance(amount)
		if outcome == 1:
			if odds > 0:
				self.increaseBalance(amount*(odds/100))
			if odds < 0:
				self.increaseBalance(amount/((-1*odds)/100))

	def getBalance(self):
		return self.balance

	def printBalance(self):
		print("$"+str(self.balance))

	def increaseBalance(self, amount):
		self.balance = self.balance + amount

	def decreaseBalance(self, amount):
		self.balance = self.balance - amount

class BasePaymentGateway:
	def __init__(self, repeat=0):
		self.repeat = repeat
		self.gateway = None
	
	def pay(self, amount,user, gateway=None):
                if gateway is None:
                        gateway = self.gateway
                self.repeat -= 1
                print("payment of {} of amount {} is sucessful by {}".format(user,amount, self.gateway))
                return True

class CheapPaymentGateway(BasePaymentGateway):
	def __init__(self, repeat=0):
		super(CheapPaymentGateway, self).__init__(repeat)
		self.gateway = "CheapPaymentGateway"

class ExpensivePaymentGateway(BasePaymentGateway):
	def __init__(self, repeat=1):
		super(ExpensivePaymentGateway, self).__init__(repeat)
		self.gateway = "ExpensivePaymentGateway"

class PremiumPaymentGateway(BasePaymentGateway):
	def __init__(self, repeat=3):
		super(PremiumPaymentGateway, self).__init__(repeat)
		self.gateway = "PremiumPaymentGatway"


class ProcessPayment:
	def __init__(self, amount,user):
                self.amount=amount
                self.user=user
	
	def payment(self):
		try:
			mode = None
			if self.amount <= 20:
			        mode = CheapPaymentGateway()
			elif 20 < self.amount < 500:
				mode = ExpensivePaymentGateway()
			elif self.amount >= 500:
				mode = PremiumPaymentGateway()
			else:
				return False
			
			status = mode.pay(self.amount,self.user)
			return status
		except:
			return False

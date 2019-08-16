from RAM import RAM
from DEBUG import DEBUG

class BUS():

	def SEND(self, ADDR, BYTE):	# Send Function
		pass
	
	def RECEIVE(self): # Receive Function
		BYTE = DATA().READ()
		DEBUG().MSG('BUS', 'RECEIVE', 'DATA', BYTE)
		return BYTE

	def PUSH(self, BYTE): # Push Function
		ADDR().PUSH(BYTE)

	def POP(self): # POP Function
		ADDR().POP()

class DATA():

	def READ(self):
		if RAM().ADDRESS[ADDR().PEEK()]:
			DATA = RAM().ADDRESS[ADDR().PEEK()]
		else:
			DATA = 0
		DEBUG().MSG('BUS', 'DATA', 'BYTE', DATA)
		return DATA

class ADDR():

	ADDRESS = []

	def __init__(self):
		pass

	def PUSH(self, BYTE):
		self.ADDRESS.append(BYTE)
		DEBUG().MSG('BUS', 'ADDR', 'PUSH', BYTE)

	def POP(self):
		DEBUG().MSG('BUS', 'ADDR', 'POP', self.PEEK())
		self.ADDRESS.pop()

	def PEEK(self):
		return self.ADDRESS[-1]
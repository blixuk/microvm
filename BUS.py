from RAM import RAM

class BUS:

	def __init__(self):
		self.WIDTH = 8
		self.DATABUS = DATA()
		self.ADDRBUS = ADDR()

	def SEND(self, ADDR, DATA):
		pass
	
	def RECEIVE(self):
		# DEBUG ======================= #
		print('BUS: RECEIVE: ' + str(self.ADDRBUS.PEEK())) #

		return self.DATABUS.DATA(self.ADDRBUS.PEEK())

	def PUSH(self, ADDR):
		self.ADDRBUS.PUSH(ADDR)
		# DEBUG ======================= #
		print('BUS: PUSH: ' + str(ADDR)) #

	def POP(self):
		# DEBUG ======================= #
		print('BUS: POP: ' + self.ADDRBUS.PEEK()) #

		self.ADDRBUS.POP()

class DATA():

	def __init__(self):
		self.WIDTH = 8
		self.BYTE = []
		self.RAM = RAM()

	def DATA(self, ADDR):
		if ADDR in self.RAM.ADDRESS:
			DATA = self.RAM.ADDRESS[ADDR]
		else:
			DATA = None

		# DEBUG ======================= #
		print('BUS: DATA: ' + str(DATA)) #

		self.BYTE = []
		while DATA:
			if DATA != None:
				if DATA[0] != None:
					self.BYTE.append(DATA[:self.WIDTH])
					DATA = DATA[self.WIDTH:]
				else:
					self.BYTE = [None]
					break
			else:
				self.BYTE = [None]
				break

		return self.BYTE

class ADDR:

	def __init__(self):
		self.ADDR = []

	def PUSH(self, ADDR):
		self.ADDR.append(ADDR)

	def POP(self):
		self.ADDR.pop()

	def PEEK(self):
		return self.ADDR[-1]
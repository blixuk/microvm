from RAM import RAM
from DEBUG import DEBUG

class BUS():

	def SEND(self, BYTE):	# Send Function
		pass
	
	def RECEIVE(self): # Receive Function
		BYTE = DATA().READ() # Read bytes from RAM
		DEBUG().MSG('BUS', 'RECEIVE', 'DATA', hex(BYTE))
		return BYTE # Return the bytes

	def PUSH(self, BYTE): # Push Function
		ADDR().PUSH(BYTE) # Push the bytes to the Address BUS

	def POP(self): # POP Function
		ADDR().POP() # Pop the Address of the BUS

class DATA():

	def READ(self): # Read Function
		# Check if there is a value at the current address
		if RAM().ADDRESS[ADDR().PEEK()]:
			DATA = RAM().ADDRESS[ADDR().PEEK()] # Assign the value from address
		else:
			DATA = 0 # If no value assign 0
		DEBUG().MSG('BUS', 'DATA', 'BYTE', hex(DATA))
		return DATA # Return the value

class ADDR():

	ADDRESS = [] # Address register

	def PUSH(self, BYTE): # Push Function
		self.ADDRESS.append(BYTE) # Append the current byte the address register
		DEBUG().MSG('BUS', 'ADDR', 'PUSH', hex(BYTE))

	def POP(self): # Pop Function
		DEBUG().MSG('BUS', 'ADDR', 'POP', hex(self.PEEK()))
		self.ADDRESS.pop() # Remove the last address from the address register

	def PEEK(self): # Peek Function
		return self.ADDRESS[-1] # Return the top value on the address register
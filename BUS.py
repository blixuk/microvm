from RAM import RAM
from DEBUG import DEBUG

class BUS():

	def SEND(self, BYTE):	# Send Function
		DATA().WRITE(BYTE) # Write bytes to RAM
		DEBUG().MSG('BUS', 'SEND', 'DATA', BYTE)

	def RECEIVE(self): # Receive Function
		BYTE = DATA().READ() # Read bytes from RAM
		DEBUG().MSG('BUS', 'RECEIVE', 'DATA', BYTE)
		return BYTE # Return the bytes

	def PUSH(self, BYTE): # Push Function
		ADDR().PUSH(BYTE) # Push the bytes to the Address BUS

	def POP(self): # POP Function
		ADDR().POP() # Pop the Address of the BUS

	def LOAD(self, BYTE):
		DATA().LOAD(BYTE)

	def CLEAR(self):
		DATA().CLEAR()

	def LIST(self):
		print(RAM().ADDRESS)

class DATA():

	def READ(self): # Read Function
		# Check if there is a value at the current address
		if RAM().ADDRESS[ADDR().PEEK()]:
			DATA = RAM().ADDRESS[ADDR().PEEK()] # Assign the value from address
		else:
			DATA = 0 # If no value assign 0
		DEBUG().MSG('BUS', 'DATA', 'READ', DATA)
		return DATA # Return the value

	def WRITE(self, BYTE):
		# Check if there is a value at the current address
		if RAM().ADDRESS[ADDR().PEEK()]:
			RAM().ADDRESS[ADDR().PEEK()] = BYTE # Write to Address
			DEBUG().MSG('BUS', 'DATA', 'WRITE', DATA)
		else:
			DEBUG().MSG('BUS', 'DATA', 'WRITE', 'NO ADDRESS')

	def LOAD(self, BYTE):
		#RAM().ADDRESS.append(bytes(BYTE)) # Add Byte to next RAM Address
		RAM().ADDRESS.append(BYTE)
		DEBUG().MSG('BUS', 'DATA', 'LOAD', BYTE)

	def CLEAR(self):
		RAM().ADDRESS.clear() # Clear all values from RAM
		DEBUG().MSG('BUS', 'DATA', 'CLEAR', 0)

class ADDR():

	ADDRESS = [] # Address register

	def PUSH(self, BYTE): # Push Function
		self.ADDRESS.append(BYTE) # Append the current byte the address register
		DEBUG().MSG('BUS', 'ADDR', 'PUSH', BYTE)

	def POP(self): # Pop Function
		DEBUG().MSG('BUS', 'ADDR', 'POP', self.PEEK())
		self.ADDRESS.pop() # Remove the last address from the address register

	def PEEK(self): # Peek Function
		return self.ADDRESS[-1] # Return the top value on the address register
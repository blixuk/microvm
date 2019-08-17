import time

from BUS import BUS
from BUS import ADDR
from DEBUG import DEBUG

class CPU():

	def __init__(self):
		self.TICKS = 1					# Clock speed
		self.TPS = 1. / self.TICKS		# Ticks per second
		self.END = 0					# Stop Processing
		self.PC = 0						# Program Counter
		self.IR = 0						# Instruction Register
		self.AC = 0						# Accumulator

	def RUN(self, ARG): # Run Procedure
		DEBUG().DEBUG(ARG) # Enable / Disable Debug Messages
		DEBUG().MSG('CPU','RUN','CMD','DEBUG')
		DEBUG().MSG('CPU','RUN','CMD','START')
		self.CLOCK() # Start the Clock Cycle

	def CLOCK(self): # Clock Procedure
		while(self.END != 1):
			self.FETCH()	# Fetch Cycle
			self.TICK()		# Tick Cycle
			self.DECODE()	# Decode Cycle
			self.TICK()		# Tick Cycle
			self.EXECUTE()	# Execute Cycle
			self.TICK()		# Tick Cycle
			self.COUNT()	# Count Cycle
			self.TICK()		# Tick Cycle

	def FETCH(self): # Fetch Procedure
		# Send the current Address form the Program Counter to the BUS
		BUS().PUSH(self.PC)
		# Read the Instruction from RAM at the Address location on the BUS
		# into the Instruction Register
		self.READ()

	def DECODE(self): # Decode Procedure
		DEBUG().MSG('CPU', 'DECODE', 'IR', hex(self.IR))

		# COUNTER = 0
		# for BYTE in self.IR:
		# 	self.BUGMSG('CPU', 'DECODE', 'BYTE', '[' +str(COUNTER) + '] ' + str(BYTE))
		# 	COUNTER += 1

		# Remove the last Address from the BUS
		BUS().POP()

	def EXECUTE(self): # Execute Procedure
		# DEBUG ====================================== #
		if self.IR == 0: #
			DEBUG().MSG('CPU', 'EXECUTE', 'CMD', 'END')
			self.END = 1
		elif self.IR == 255:
			DEBUG().MSG('CPU', 'EXECUTE', 'CMD', 'MAX')

	def COUNT(self): # Count Procedure
		# Take the current Step value and convert into a Binary number
		# and store it into the Program Counter as the next Address
		#self.PC = bin(self.STEP)[2:].zfill(8) # Binary Counter
		self.PC += 1	# Increment the Program Counter by 1
		DEBUG().MSG('CPU', 'COUNT', 'PC', self.PC)

	def TICK(self): # Tick Procedure
		time.sleep(self.TPS)	# Sleep cycle based on set TPS

	def READ(self): # Read Procedure
		self.IR =  BUS().RECEIVE()
	
	def WRITE(self, ADDR, DATA): # Write Procedure
		pass

# Commands
# HEX: 00 | ASM: END - End Operation
# HEX: 01 | ASM: --
# HEX: 02 | ASM: --
# HEX: 03 | ASM: --
# HEX: 04 | ASM: --
# HEX: 05 | ASM: --
# HEX: 06 | ASM: --
# HEX: 07 | ASM: --
# HEX: 08 | ASM: --
# HEX: 09 | ASM: --
# HEX: 0A | ASM: --
# HEX: 0B | ASM: --
# HEX: 0C | ASM: --
# HEX: 0D | ASM: --
# HEX: 0E | ASM: --
# HEX: 0F | ASM: --

# HEX: FF | ASM: NOP - No Operation
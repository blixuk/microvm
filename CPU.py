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
		self.IR = hex(self.IR)[2:].zfill(2) # Remove 0x and fill with 0
		DEBUG().MSG('CPU', 'DECODE', 'IR', self.IR)
		self.AC = self.IR[1:] # Put the 2nd value into the Accumulator
		DEBUG().MSG('CPU', 'DECODE', 'AC', self.AC)
		# Remove the last Address from the BUS
		BUS().POP()

	def EXECUTE(self): # Execute Procedure
		# DEBUG ====================================== #
		if self.IR[:1] == '0':
			DEBUG().MSG('CPU', 'EXECUTE', 'CMD', 'END')
			self.END = 1
		elif self.IR[:1] == 'f':
			DEBUG().MSG('CPU', 'EXECUTE', 'CMD', 'NOP')

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
# HEX: 0 | ASM: END - End Operation
# HEX: 1 | ASM: --
# HEX: 2 | ASM: --
# HEX: 3 | ASM: --
# HEX: 4 | ASM: --
# HEX: 5 | ASM: --
# HEX: 6 | ASM: --
# HEX: 7 | ASM: --
# HEX: 8 | ASM: --
# HEX: 9 | ASM: --
# HEX: A | ASM: --
# HEX: B | ASM: --
# HEX: C | ASM: --
# HEX: D | ASM: --
# HEX: E | ASM: --
# HEX: F | ASM: NOP - No Operation
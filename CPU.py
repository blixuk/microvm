import time

from BUS import BUS
from DEBUG import DEBUG

class CPU():

	def __init__(self):
		self.TICKS = 1					# Clock speed
		self.TPS = 1. / self.TICKS		# Ticks per second
		self.END = 0					# Stop Processing
		self.PC = 0						# Program Counter
		self.IR = 0						# Instruction Register
		self.AC = 0						# Accumulator

	def RUN(self): # Run Procedure
		#DEBUG().DEBUG(BUG) # Enable / Disable Debug Messages
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
		#self.IR = hex(self.IR)[2:].zfill(2) # Remove 0x and fill with 0
		CMD = int.from_bytes(self.IR[:1], byteorder='little')
		VAL = int.from_bytes(self.IR[1:], byteorder='little')
		self.IR = [CMD, VAL]
		#print(int.from_bytes(self.IR, byteorder='little'))
		DEBUG().MSG('CPU', 'DECODE', 'IR', self.IR)
		BUS().POP() # Pop Address from the BUS

	def EXECUTE(self): # Execute Procedure
		if self.IR[0] == 0:
			DEBUG().MSG('CPU', 'EXECUTE', 'CMD', 'END') # END OPERATION
			self.END = 1
		elif self.IR[0] ==  15:
			DEBUG().MSG('CPU', 'EXECUTE', 'CMD', 'NOP') # NO OPERATION
			pass
		elif self.IR[0] ==  14:
			DEBUG().MSG('CPU', 'EXECUTE', 'CMD', 'NUM') # JUMP
			DEBUG().MSG('CPU', 'JMP', 'PC', self.IR[1])
		elif self.IR[0] ==  1:
			DEBUG().MSG('CPU', 'EXECUTE', 'CMD', 'LOD') # LOAD
			BUS().PUSH(self.IR[1]) # Push Address to BUS
			self.AC = int.from_bytes(BUS().RECEIVE()[1:], byteorder='little') # Add to Accumulator from RAM
			DEBUG().MSG('CPU', 'LOD', 'AC', self.AC)
			BUS().POP() # Pop Address from BUS
		elif self.IR[0] ==  2:
			DEBUG().MSG('CPU', 'EXECUTE', 'CMD', 'STR') # STORE
			BUS().PUSH(self.IR[1]) # Push Address to BUS
			self.WRITE() # Write Accumulator to RAM
			DEBUG().MSG('CPU', 'STR', 'AC', self.AC)
			BUS().POP() # Pop Address from BUS
		elif self.IR[0] ==  3:
			DEBUG().MSG('CPU', 'EXECUTE', 'CMD', 'ADD') # ADD
			BUS().PUSH(self.IR[1]) # Push Address to BUS
			self.AC += int.from_bytes(BUS().RECEIVE()[1:], byteorder='little') # Add to Accumulator from RAM
			DEBUG().MSG('CPU', 'ADD', 'AC', self.AC)
			BUS().POP() # Pop Address from BUS
		elif self.IR[0] ==  4:
			DEBUG().MSG('CPU', 'EXECUTE', 'CMD', 'SUB') # SUB
			BUS().PUSH(self.IR[1]) # Push Address to BUS
			self.AC -= int.from_bytes(BUS().RECEIVE()[1:], byteorder='little') # Sub from Accumulator from RAM
			DEBUG().MSG('CPU', 'SUB', 'AC', self.AC)
			BUS().POP() # Pop Address from BUS
		elif self.IR[0] ==  5:
			DEBUG().MSG('CPU', 'EXECUTE', 'CMD', 'JMP') # JUMP
			self.PC = int.from_bytes(self.IR[1:], byteorder='little') - 1 # Change Program Counter value
			DEBUG().MSG('CPU', 'JMP', 'PC', self.PC + 1)

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
	
	def WRITE(self): # Write Procedure
		BUS().SEND((self.AC).to_bytes(1, byteorder='little')) # Push the Accumulator value to RAM

	def LOAD(self, BIN):
		DEBUG().MSG('CPU','LOAD','BIN', BIN)
		DATA = open(BIN, "rb")
		BUS().CLEAR()
		BYTE = DATA.readlines()

		counter = []

		for BIT in BYTE[0]:
			counter.append(BIT)

			if len(counter) == 2:
				CMD = (counter[0]).to_bytes(2, byteorder='little')
				VAL = (counter[1]).to_bytes(2, byteorder='little')
				BUS().LOAD(CMD[:1] + VAL[:1])
				counter.clear()
		
		self.RUN()

# Commands
#  0 HEX: 00 | ASM: END - End Operation
#  1 HEX: 01 | ASM: LOD - Load into Accumulator
#  2 HEX: 02 | ASM: STR - Store Accumulator in Address
#  3 HEX: 03 | ASM: ADD - Add to Accumulator
#  4 HEX: 04 | ASM: SUB - Sub from Accumulator
#  5 HEX: 05 | ASM: JMP - Jump to Address
#  6 HEX: 06 | ASM: --
#  7 HEX: 07 | ASM: --
#  8 HEX: 08 | ASM: --
#  9 HEX: 09 | ASM: --
# 10 HEX: 0A | ASM: --
# 11 HEX: 0B | ASM: --
# 12 HEX: 0C | ASM: --
# 13 HEX: 0D | ASM: --
# 14 HEX: 0E | ASM: NUM - Number
# 15 HEX: 0F | ASM: NOP - No Operation
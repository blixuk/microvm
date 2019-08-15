import time

from BUS import BUS

class CPU():

	def __init__(self):
		self.TICKS = 1					# Clock speed
		self.TPS = 1. / self.TICKS		# Ticks per second
		self.HALT = 0					# Stop Processing
		self.DEBUG = 0					# Show Debug Messages
		self.STEP = 0					# Step Counter
		self.PC = 0						# Program Counter
		self.IR = 0						# Instruction Register
		self.AC = 0						# Accumulator
		self.ST = STACK()				# Stack
		self.CACHE = [lambda: self.PC, lambda: self.IR, lambda: self.AC, lambda: self.ST]	# Cache Memory

		self.BUS = BUS()

	def RUN(self, DEBUG):		# CPU Run Procedure
		self.DEBUG = DEBUG
		self.BUGMSG('CPU','RUN','CMD','DEBUG')
		self.BUGMSG('CPU','RUN','CMD','START')
		self.CLOCK()

	def CLOCK(self):	# CPU Clock Procedure
		while(self.HALT != 1):
			self.COUNT()			# On each cycle Count
			self.FETCH()			# On each cycle Fetch
			self.DECODE()			# On each cycle Decode
			self.EXECUTE()			# On each cycle Execute
			self.TICK()				# On each cycle Tick

	def FETCH(self):	# CPU Fetch Procedure
		# Send the current Address form the Program Counter to the BUS
		self.BUS.PUSH(self.PC)
		# Read the Instruction from RAM at the Address location on the BUS
		# into the Instruction Register
		self.IR = self.READ()

	def DECODE(self):	# CPU Decode Procedure
		self.BUGMSG('CPU', 'DECODE', 'IR', self.IR)

		COUNTER = 0
		for BYTE in self.IR:
			self.BUGMSG('CPU', 'DECODE', 'BYTE', '[' +str(COUNTER) + '] ' + str(BYTE))
			COUNTER += 1

		# Remove the last Address from the BUS
		self.BUS.POP()

	def EXECUTE(self):	# CPU Execute Procedure
		# DEBUG ====================================== #
		if self.IR[0] == None: #
			self.HALT = 1 #
			self.BUGMSG('CPU', 'EXECUTE', 'CMD', 'HALT')

	def COUNT(self):	# CPU Count Procedure
		# Take the current Step value and convert into a Binary number
		# and store it into the Program Counter as the next Address
		self.PC = bin(self.STEP)[2:].zfill(8)
		self.STEP += 1	# Increment the Step Counter by 1
		# DEBUG ====================================== #
		self.BUGMSG('CPU', 'COUNT', 'STEP', self.STEP)
		self.BUGMSG('CPU', 'COUNT', 'PC', self.PC)

	def TICK(self):		# CPU Tick Procedure
		time.sleep(self.TPS)	# Sleep cycle based on set TPS

	def READ(self):		# CPU Read Procedure
		return self.BUS.RECEIVE()
	
	def WRITE(self, ADDR, DATA):
		pass

	def BUGMSG(self, NME, PROS, CMD, MSG):	# DEBUG MESSAGE
		if self.DEBUG != 1:
			print('[{0}] {1}: {2}: {3}: {4}').format(str(self.STEP), str(NME),str(PROS), str(CMD), str(MSG))

class STACK:
	def __init__(self):
		self.STACK = []

	def PUSH(self, DATA):
		self.STACK.append(DATA)

	def POP(self):
		self.STACK.pop()

	def PEEK(self):
		return self.STACK[-1]

	def NONE(self):
		return self.STACK == []
	
	def COUNT(self):
		return len(self.STACK)

	def STACK(self):
		return self.STACK

	def DUMP(self):
		while self.STACK:
			yield self.STACK.pop()

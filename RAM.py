class RAM:

	def __init__(self):
		self.ADDRESS = bytearray(b'\x16\x37\x26\x51\xf0\xf0\x01\x01')

		# Counter
		# 16 LOD 6
		# 37 ADD 7
		# 26 STR 6
		# 51 JMP 1
		# f0 NOP
		# f0 NOP
		# 01 1
		# 01 1
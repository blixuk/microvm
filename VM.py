import sys

from CPU import CPU
from DEBUG import DEBUG

def main():
	print(sys.argv)

	# if len(sys.argv) > 2:
	# 	if sys.argv[2] == 'true':
	# 		DEBUG().ON()
	# 	if sys.argv[2] == 'false':
	# 		DEBUG().OFF()
	if len(sys.argv) == 2:
		if sys.argv[1].endswith('.bin'):
			CPU().LOAD(sys.argv[1])
		else:
			print('Please select a microVM BIN file!')
	elif len(sys.argv) == 3:
		if sys.argv[1] == '--compile' or sys.argv[1] == '-c':
			if sys.argv[2].endswith('.mvm'): 
				compile(sys.argv[2])
			else:
				print('Please select a microVM source file!')
	else:
		print('microVM: A Micro Virtual Machine!')
		print('')
		print('Options:')
		print('<bin>			| ex: mvm test.bin')
		print('-c <file>		| ex: mvm -c test.mvm | --compile')
		print('')

	#CPU().RUN()

def compile(file):
	source = open(file, 'r')
	parse = []
	for line in source.readlines():
		if line.startswith('#'):
			pass
		elif line == '\n':
			pass
		elif line == '\t':
			pass
		else:
			line = line.rstrip()
			if ' ' in line:
				CMD = line.split(' ')[0]
				VAL = line.split(' ')[1]
			else:
				CMD = line

			if CMD == 'END':
				print('END')
				CMD = (0).to_bytes(1, byteorder='little')
				VAL = (0).to_bytes(1, byteorder='little')
				parse.append(CMD + VAL)
			elif CMD == 'LOD':
				print('LOD ' + VAL)
				CMD = (1).to_bytes(1, byteorder='little')
				VAL = (int(VAL)).to_bytes(1, byteorder='little')
				parse.append(CMD + VAL)
			elif CMD == 'STR':
				print('STR ' + VAL)
				CMD = (2).to_bytes(1, byteorder='little')
				VAL = (int(VAL)).to_bytes(1, byteorder='little')
				parse.append(CMD + VAL)
			elif CMD == 'ADD':
				print('ADD '  + VAL)
				CMD = (3).to_bytes(1, byteorder='little')
				VAL = (int(VAL)).to_bytes(1, byteorder='little')
				parse.append(CMD + VAL)
			elif CMD == 'SUB':
				print('SUB '  + VAL)
				CMD = (4).to_bytes(1, byteorder='little')
				VAL = (int(VAL)).to_bytes(1, byteorder='little')
				parse.append(CMD + VAL)
			elif CMD == 'JMP':
				print('JMP ' + VAL)
				CMD = (5).to_bytes(1, byteorder='little')
				VAL = (int(VAL)).to_bytes(1, byteorder='little')
				parse.append(CMD + VAL)
			elif CMD == 'NOP':
				print('NOP 0')
				CMD = (15).to_bytes(1, byteorder='little')
				VAL = (0).to_bytes(1, byteorder='little')
				parse.append(CMD + VAL)
			elif CMD == 'NUM':
				print('NUM ' + VAL)
				CMD = (14).to_bytes(1, byteorder='little')
				VAL = (int(VAL)).to_bytes(1, byteorder='little')
				parse.append(CMD + VAL)
			else:
				print(CMD)

	source.close()
	binary = open(file.replace('.mvm', '.bin'), 'ab')

	for byte in parse:
		print(byte)
		binary.write(byte)

if __name__ == "__main__":
	main()

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
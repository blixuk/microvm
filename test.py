
def main():
	ADDRESS = bytearray(b'\x00\xFF\xEE\x10\x00')
	print(ADDRESS)
	print(ADDRESS[0])
	print(ADDRESS[1])
	ADDRESS[0] = 16
	print(hex(ADDRESS[0])[2:])
	print(hex(15)[2:])

	print(bytes(0))


if __name__ == "__main__":
	main()
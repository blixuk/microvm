class RAM:

	def __init__(self):
		self.ADDRESS = {
			'00000000' : [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			'00000001' : [0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1],
			'00000010' : [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
			'00000011' : [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			'00000100' : [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
			'00000101' : [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
			'00000110' : [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
			'00000111' : [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
		
			'00001000' : None,
			'00001001' : None,
			'00001010' : None,
			'00001011' : None,
			'00001100' : None,
			'00001101' : None,
			'00001110' : None,
			'00001111' : None
		}
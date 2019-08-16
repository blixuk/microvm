class DEBUG():

	DEBUG = 0

	def __init__(self):
		pass

	def DEBUG(self, ARG):
		self.DEBUG = ARG

	def MSG(self, NME, PROS, CMD, MSG):
		if self.DEBUG != 1:
			print('| {0}: {1}: {2}: {3}').format(str(NME), str(PROS), str(CMD), str(MSG))
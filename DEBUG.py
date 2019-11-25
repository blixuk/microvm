class DEBUG():

	ENABLED = True

	def ON(self):
		self.ENABLED = True
		print(self.ENABLED)

	def OFF(self):
		self.ENABLED = False
		print(self.ENABLED)

	def MSG(self, NME, PROS, CMD, MSG):
		if self.ENABLED == True:
			print(f'| {str(NME)}: {str(PROS)}: { str(CMD)}: {str(MSG)}')
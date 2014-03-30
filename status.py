import time

class Status:
	def __init__(self):
		#self.privacy = "public"
		self.time = time.asctime(time.localtime(time.time()))
		self.status = ""
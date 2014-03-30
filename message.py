import time

class Message:
	def __init__(self):
		self.sender = ""
		self.receiver = []
		self.time = time.asctime(time.localtime(time.time()))
		self.title = "No Title"
		self.message = ""
		self.status = "Unread"
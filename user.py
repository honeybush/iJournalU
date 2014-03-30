from Tkinter import*
#from datetime import datetime

class User:
	def __init__(self):
		self.username = ""
		self.password = ""
		self.firstname = ""
		self.lastname = ""
		self.gender = ""
		self.birthdate = 0
		self.birthmonth = 0
		self.birthyear = 0
		self.age = 0
		self.eduHistory = ""
		self.jobHistory = ""
		self.dp = self.username + "_dp.gif"
		self.userInfo = {}
		self.userPass = {}
		self.status = ""
		self.allStats = {}
		self.friends = []
	def reset(self):
		self.username = ""
		self.password = ""
		self.firstname = ""
		self.lastname = ""
		self.gender = ""
		self.birthdate = 0
		self.birthmonth = 0
		self.birthyear = 0
		self.age = 0
		self.eduHistory = ""
		self.jobHistory = ""
		self.dp = self.username + "_dp.gif"
		self.userInfo = {}
		self.userPass = {}
		self.status = ""
		self.allStats = {}
		self.friends = []
#	def convertBirthday(self):
#		now = str(datetime.now())
#		print now
	def sendInfo(self):
		self.userInfo["firstname"] = self.firstname
		self.userInfo["lastname"] = self.lastname
		self.userInfo["gender"] = self.gender
		self.userInfo["birthdate"] = self.birthdate
		self.userInfo["birthmonth"] = self.birthmonth
		self.userInfo["birthyear"] = self.birthyear
		self.userInfo["age"] = self.age
		self.userInfo["eduHistory"] = self.eduHistory
		self.userInfo["jobHistory"] = self.jobHistory
		self.userInfo["dp"] = self.dp
		return self.userInfo
	def sendUserPass(self):
		username = self.username
		password = self.password
		self.userPass["username"] = username
		self.userPass["password"] = password
		return self.userpass
user = User()
#user.convertBirthday()
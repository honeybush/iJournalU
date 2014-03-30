from Tkinter import*
import all_factory

class CC:
	def __init__(self):
		self.log_in = {}
		self.online = False
		self.new_user = {}
		self.userlist = {}
		self.userinfo = {}
		self.searchinfo = {}
		self.factory = all_factory.Factory()
		self.user = self.factory.openUser(self.userinfo)
		self.status = ""
		self.message = {}
		self.allStats = {}
		self.request = {}
		self.friends = []
	def createUser(self):
		self.factory.createUser(self.new_user)
	def getUserList(self):
		f = open("userlist.txt", "r")
		allusers = []
		for line in f:
			if line[0] != "\t":
				allusers.append(line)
		for users in allusers:
			temp = users.split()
			temp_2 = temp[0]
			self.userlist[temp_2[:len(temp_2)-1]] = temp[1]
		f.close
	def searchUser(self, username):
		self.getUserList()
		for users in self.userlist.keys():
			if users == username:
				return True
		return False
	def confirmPass(self, username, password):
		if self.userlist.get(username) == password:
			return True
		else:
			return False
	def login(self):
		username = self.log_in.get("Username")
		password = self.log_in.get("Password")
		temp_1 = self.searchUser(username)
		temp_2 = self.confirmPass(username, password)
		
		if temp_1 == temp_2 == True:
			self.getUserInfo(username)
			self.user = self.factory.openUser(self.userinfo)
			self.online = True
			return True
		else:
			self.error()
			return False
	def getUserInfo_t(self, username):
		temp = []
		userinfo = {}
		f = open(username+".txt", "r")
		for lines in f:
			temp.append(lines)
		userpass = temp[0].split(":")
		userinfo["username"] = userpass[0]
		userinfo["password"] = userpass[1].rstrip()
		name = temp[1].split(",")
		userinfo["lastname"] = name[0]
		userinfo["firstname"] = name[1].rstrip()
		userinfo["gender"] = temp[2].rstrip()
		birthday = temp[3].split()
		userinfo["birthdate"] = birthday[0]
		userinfo["birthmonth"] = birthday[1]
		userinfo["birthyear"] = birthday[2]
		userinfo["dp"] = temp[4].rstrip()
		n = 5
		eh = ""
		jh = ""
		for i in temp[n:]:
			if i[0:2] == "JH":
				break
			else:
				eh = eh + i
				n = n+1
		for j in temp[n:]:
			jh = jh + j
			n= n+1
		userinfo["eduHistory"] = eh[4:len(eh)-1]
		userinfo["jobHistory"] = jh[4:len(eh)-1]
		f.close()
		return userinfo
	def getUserInfo(self, username):
		self.userinfo = self.getUserInfo_t(username)
	def getSearchInfo(self, username):
		self.searchinfo = self.getUserInfo_t(username)
	def error(self):
		self.online = False
	def newStatus(self):
		self.user.status = self.status
		self.factory.createStatus(self.user.username, self.user.status)
	def newMessage(self):
		self.factory.createMess(self.message)
	def _setAllStats(self, username):
		try:
			allStats = {}
			f = open(username+"_status.txt", "r")
			temp = ""
			for line in f:
				if line[0] == "\t":
					allStats[temp] = line[1:len(line)-1]
				else:
					temp = line.rstrip()
			f.close()
			return allStats
		except:
			pass
	def _getAllStats(self, username):
		_allStats = self._setAllStats(username)
		return _allStats
	def getAllStats(self):
		self.allStats = self._getAllStats(self.user.username)
	def getFriendsList(self, username):
		f = open("userlist.txt")
		n = 0
		for lines in f:
			if lines[:len(username)] == username:
				break
			n = n+1
		i = 0
		friends = []
		for lines in f:
			if i<=n:
				pass
			if lines[0:1] == "\t":
				friends.append(lines[1:len(lines)-1])
			if not(lines[0:1] == "\t"):
				break
			i = i+1
		f.close()
		return friends
	def getFriends(self):
		self.friends = self.user.friends = self.getFriendsList(self.user.username)
		return self.friends
cc = CC()
from Tkinter import*
import user
import status
import message

class Factory:
	def openUser(self, userInfo):
		person = user.User()
		
		person.username = userInfo.get("username")
		person.password = userInfo.get("password")
		person.firstname = userInfo.get("firstname")
		person.lastname = userInfo.get("lastname")
		person.gender = userInfo.get("gender")
		person.birthdate = userInfo.get("birthdate")
		person.birthmonth = userInfo.get("birthmonth")
		person.birthyear = userInfo.get("birthyear")
		person.eduHistory = userInfo.get("eduHistory")
		person.jobHistory = userInfo.get("jobHistory")
		person.dp = userInfo.get("dp")
		return person
	def createUser(self, userInfo):
		user = self.openUser(userInfo)
		
		f = open(user.username+".txt", "w")
		f.write(user.username + ": " + user.password + "\n")
		f.write(user.lastname + ", " + user.firstname + "\n")
		f.write(user.gender + "\n")
		f.write(user.birthdate + " " + user.birthmonth + " " + user.birthyear + "\n")
		f.write(user.dp + "\n")
		f.write("EH: " + user.eduHistory)
		f.write("JH: " + user.jobHistory)
		f.close()
		
		g = open("userlist.txt", "a")
		g.write("\n" + user.username + ": " + user.password)
		g.close()
	def photoCount(self): #make a counter here
		print "-"
	def createStatus(self, user, _status):
		stat = status.Status()
		stat.status = _status
		f = open(user+"_status.txt", "a")
		f.write(str(stat.time+"\n"))
		f.write("\t"+_status+"\n")
		f.close()
	def createMess(self, info):
		mess = message.Message()
		mess.sender = info.get("sender")
		mess.receiver = info.get("receiver")
		mess.title = info.get("title")
		mess.message = info.get("message")
		
		f = open(mess.sender+"_mail.txt", "a")
		f.write(str(mess.time)+"\n\t"+mess.sender+"="+str(mess.receiver)+"\n")
		f.write("\t"+"Sender"+"\n\t\t"+mess.title+"\n\t\t\t"+mess.message+"\n")
		f.close
		
		for person in mess.receiver:
			g = open(person+"_mail.txt", "a")
			g.write(str(mess.time)+"\n\t"+mess.sender+":"+str(mess.receiver)+"\n")
			g.write("\t"+mess.status+"\n\t\t"+mess.title+"\n\t\t\t"+mess.message+"\n")
			g.close()
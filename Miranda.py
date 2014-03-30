from Tkinter import*
import control_center
import Tkconstants, tkFileDialog, tkMessageBox
from PIL import Image, ImageTk

class MainMenu:
	def __init__(self, root):
		self.cc = control_center.CC()
		self.newUserInfo = {}
		
		self.root = root
		self.root.geometry("640x480")
		self.root.resizable(width=FALSE, height=FALSE)
		self.heading = "iJournal.U"
		self.root.title(self.heading)
		self.iconpic = PhotoImage(file="icon.gif")
		self.root.tk.call('wm', 'iconphoto', self.root._w, self.iconpic)
		self.root.grid()
		
		self.menubar = Menu(self.root)
		
		self.filemenu = Menu(self.menubar)
		self.filemenu.add_command(label="Create Account", command=self.newaccount)
		self.filemenu.add_command(label="Log in", command=self.login)
		self.filemenu.add_command(label="Log Out", command=self.logout)
		self.filemenu.add_separator()
		self.filemenu.add_command(label="Exit", command=self.root.destroy)
		self.menubar.add_cascade(label="File", menu=self.filemenu)
		
		self.viewmenu = Menu(self.menubar)
		self.viewmenu.add_command(label="Profile", command=self.profile)
		self.viewmenu.add_command(label="News Feed", command=self.newsfeed)
		self.viewmenu.add_command(label="Messages", command=self.messages)
		self.viewmenu.add_command(label="Friends", command=self.friends)
		self.viewmenu.add_command(label="Search", command=self.search)
		self.viewmenu.add_command(label="Notifications", command=self.notif)
		self.menubar.add_cascade(label="View", menu=self.viewmenu)
		
		self.editmenu = Menu(self.menubar)
		self.editmenu.add_command(label="Edit Profile", command=self.edit_profile)
		self.menubar.add_cascade(label="Edit", menu=self.editmenu)
		
		self.helpmenu = Menu(self.menubar)
		self.helpmenu.add_command(label="Help Contents", command=self.help)
		self.helpmenu.add_separator()
		self.helpmenu.add_command(label="About", command=self.about)
		self.menubar.add_cascade(label="Help", menu=self.helpmenu)
		
		self.root.config(menu=self.menubar)
		
		self.defaultframe = DefaultFrame(self.root, self.cc)
		
		self.filemenu.entryconfig(0, state=DISABLED)
		self.viewmenu.entryconfig(0, state=DISABLED)
		self.helpmenu.entryconfig(0, state=DISABLED)
		self.editmenu.entryconfig(0, state=DISABLED)
		
		self.offlineMenu()
	def login(self):
		print "Log In"
		login = Toplevel(self.root, takefocus=True)
		popup = LogInPopUp(login, self.cc)
		if not(self.cc.user.username == ""):
			self.onlineMenu()
	def offlineMenu(self):
		self.filemenu.entryconfig(1, state=NORMAL)
		self.filemenu.entryconfig(2, state=NORMAL)
		self.filemenu.entryconfig(3, state=DISABLED)
		self.viewmenu.entryconfig(1, state=DISABLED)
		self.viewmenu.entryconfig(2, state=DISABLED)
		self.viewmenu.entryconfig(3, state=DISABLED)
		self.viewmenu.entryconfig(4, state=DISABLED)
		self.viewmenu.entryconfig(5, state=DISABLED)
		self.viewmenu.entryconfig(6, state=DISABLED)
		self.editmenu.entryconfig(1, state=DISABLED)
	def onlineMenu(self):
		self.viewmenu.entryconfig(1, state=NORMAL)
		self.viewmenu.entryconfig(2, state=NORMAL)
		self.viewmenu.entryconfig(3, state=NORMAL)
		self.viewmenu.entryconfig(4, state=NORMAL)
		self.viewmenu.entryconfig(5, state=NORMAL)
		self.filemenu.entryconfig(3, state=NORMAL)
		self.viewmenu.entryconfig(6, state=NORMAL)
		self.editmenu.entryconfig(1, state=NORMAL)
		self.filemenu.entryconfig(1, state=DISABLED)
		self.filemenu.entryconfig(2, state=DISABLED)
	def logout(self):
		self.cc.log_in = {}
		self.cc.online = False
		self.cc.new_user = {}
		self.cc.userlist = {}
		self.cc.userinfo = {}
		self.cc.status = ""
		self.cc.message = {}
		self.cc.allStats = {}
		self.offlineMenu()
		self.cc.user.reset()
	def newaccount(self):
		newaccount = newAccountFrame(self.root, self.cc)
	
	def profile(self):
		profile = Profile(self.root, self.cc)
	
	def newsfeed(self):
		print "Newsfeed"

	def messages(self):
		message = Message(self.root, self.cc)
		
	def friends(self):
		friends = Friends(self.root, self.cc)

	def search(self):
		search = Toplevel(self.root, takefocus=True)
		_search = Search(self.root, search, self.cc)

	def notif(self):
		print "Notifications"
	
	def edit_profile(self):
		editProfile = EditProfile(self.root, self.cc)
		editProfile.setInfo(self.root, self.cc)
	
	def help(self):
		help = Toplevel(self.root, takefocus=True)
		Label(help, text="Click\n\tFile>Create Account: to to join your journey with us\n\tFile>Log-in: to visit your sanctuary\n\tView: to discover different beings\n\tEdit: to manipulate your surroundings\n\n\t...and finally\n\n\tFile>log-out: to return to reality.\n\nCurrent Functions:\n-log-in/out\n-create account\n-search people\n-view friends\n-edit profile(still buggy though)\n-upload pictures(sometimes the pics appear, sometimes not.)\n-messages only work in command prompt\n-adding friends are incomplete\n-deletion not able to implement\n\nsorry for the crappy gui. ;M;").place(x=5, y=5)
	
	def about(self):
		about = Toplevel(self.root, takefocus=True)
		Label(about, text="iJournal.U ver1.0 (Beta)\nCreator: Aliya Ahlanna C. Miranda\nAdvisers: Philip Christian Zuniga, Ada Angeli Cariaga\n\nArt: Paint.NET\n\nGuidance: stackoverflow.com\n\nSpecial Thanks to:\n\t-my laptop for not dying on me\n\t-the mugs of coffee sacrificed every night\n\t-my music files for slapping me awake\n\nUPD CS12 Class Project SY13/14\n\nThanks for the challenging year :D").place(x=5, y=5)

class DefaultFrame:
	def __init__(self, root, cc):
		self.root = root
		self.cc = cc
		self.default_frame = Frame(self.root, height=480, width=640)
		self.default_frame.place(x=0, y=0)
		
		self.defaultbg = PhotoImage(file="default.gif")
	
		self.default = Label(self.default_frame, image=self.defaultbg)
		self.default.image = self.defaultbg
		self.default.place(x=0, y=0)

class LogInPopUp:
	def __init__(self, login, cc):
		self.login_details = {}
		self.cc = cc
		self.login = login
		self.login.geometry("220x100")
		self.login.grab_set()
		self.login.title("Log-in")
		self.usernameLabel = Label(self.login, text="Username: ")
		self.usernameLabel.place(x=10, y=10)
		self.username = Entry(self.login)
		self.username.place(x=75, y=10)
		self.passwordLabel = Label(self.login, text="Password: ")
		self.passwordLabel.place(x=10, y=30)
		self.password = Entry(self.login, show="*")
		self.password.place(x=75, y=30)
		self.enter = Button(self.login, text="Log-in", command=self.loginclick)
		self.enter.place(x=90, y=60)
	def loginclick(self):
		self.getLogIn()
		login = self.cc.login()
		if login == True:
			self.cc = control_center.CC()
			self.login.destroy()
		else:
			tkMessageBox.showerror("Log-In", "Incorrect username/password")
	def getLogIn(self):
		username = self.username.get()
		password = self.password.get()
		self.login_details["Username"] = username
		self.login_details["Password"] = password
		self.cc.log_in = self.login_details

class newAccountFrame:
	def __init__(self, root, cc):
		self.newUserInfo = {}
		self.cc = cc
		self.root = root
		self.new_account = Frame(self.root, height=480, width=640)
		self.new_account.place(x=0, y=0)
		canvas = Canvas(self.new_account, scrollregion=(0, 0, 480, 640), bg="light blue")
		canvas.pack(side=TOP, fill=BOTH)
		canvas.configure(height=480, width=640)
		self.label_1 = Label(canvas, text="Create Profile:")
		self.label_1.place(x=5, y=5)
		self.username = Label(canvas, text="Username: ")
		self.username.place(x=10, y=30)
		self.usernameEntry = Entry(canvas)
		self.usernameEntry.place(x=80, y=30)
		self.password = Label(canvas, text="Password: ")
		self.password.place(x=230, y=30)
		self.passwordEntry = Entry(canvas, show="*")
		self.passwordEntry.place(x=300, y=30)
		self.firstname = Label(canvas, text="First Name: ")
		self.firstname.place(x=10, y=60)
		self.firstnameEntry = Entry(canvas)
		self.firstnameEntry.place(x=80, y=60)
		self.lastname = Label(canvas, text="Last Name: ")
		self.lastname.place(x=230, y=60)
		self.lastnameEntry = Entry(canvas)
		self.lastnameEntry.place(x=300, y=60)
		self.gender = Label(canvas, text="Gender: ")
		self.gender.place(x=10, y=90)
		self.genderEntry = Entry(canvas)
		self.genderEntry.place(x=80, y=90)
		self.birthdate = Label(canvas, text="Birthday(dd/mm/yyyy): ")
		self.birthdate.place(x=10, y=120)
		self.days = ["day"]
		for i in range(1, 32):
			self.days.append(i)
		self.vardays = StringVar(canvas)
		self.vardays.set(self.days[0])
		self.choosedays = apply(OptionMenu, (canvas, self.vardays) + tuple(self.days))
		self.choosedays.place(x=30, y=145)
		self.months = ["month"]
		for i in range(1, 13):
			self.months.append(i)
		self.varmonths = StringVar(canvas)
		self.varmonths.set(self.months[0])
		self.choosemonths = apply(OptionMenu, (canvas, self.varmonths) + tuple(self.months))
		self.choosemonths.place(x=100, y=145)
		self.chooseyears = Entry(canvas)
		self.chooseyears.place(x=190, y=150)
		self.eduHistory = Label(canvas, text="Educational History: ")
		self.eduHistory.place(x=10, y=180)
		self.eduHistoryEntry = Text(canvas, height=4, width=40)
		self.eduHistoryEntry.place(x=10, y=210)
		self.jobHistory = Label(canvas, text="Job History: ")
		self.jobHistory.place(x=10, y=280)
		self.jobHistoryEntry = Text(canvas, height=4, width=40)
		self.jobHistoryEntry.place(x=10, y=310)
		self.dplabel = Label(canvas, text="Profile Picture:")
		self.dplabel.place(x=10, y=390)
		self.dp = Button(canvas, text="Upload", command=self.getpic)
		self.dp.place(x=100, y=388)
		self.dpname = ""
		self.dp_ulabel = Label(canvas, text=self.dpname)
		self.dp_ulabel.place(x=160, y=390)
		self.submit = Button(canvas, text="Submit", command=self.submitDetails)
		self.submit.place(x=10, y=420)
		
		self.file_opt = options = {}
		options['defaultextension'] = '.gif'
		options['filetypes'] = [('Image Files', '*.jpg;*.gif;*.png')]
		options['initialdir'] = 'C:\\'
		options['parent'] = canvas
	
	def getpic(self):
		self.dpname = tkFileDialog.askopenfilename(**self.file_opt)
		self.dp_ulabel.configure(text=self.dpname)
	
	def convertImage(self, dpname, username):
		image = Image.open(dpname)
		w = 150
		wp = (w/float(image.size[0]))
		h = int((float(image.size[1])*float(wp)))
		image = image.resize((w, h), Image.ANTIALIAS)
		temp = username+"_dp.gif"
		image.save(temp)
		return temp
	
	def getInfo(self):
		username = self.usernameEntry.get()
		self.dpname = self.convertImage(self.dpname, username)
		self.newUserInfo["username"] = self.usernameEntry.get()
		self.newUserInfo["password"] = self.passwordEntry.get()
		self.newUserInfo["firstname"] = self.firstnameEntry.get()
		self.newUserInfo["lastname"] = self.lastnameEntry.get()
		self.newUserInfo["gender"] = self.genderEntry.get()
		self.newUserInfo["birthdate"] = self.vardays.get()
		self.newUserInfo["birthmonth"] = self.varmonths.get()
		self.newUserInfo["birthyear"] = self.chooseyears.get()
		self.newUserInfo["eduHistory"] = self.eduHistoryEntry.get(1.0, END)
		self.newUserInfo["jobHistory"] = self.jobHistoryEntry.get(1.0, END)
		self.newUserInfo["dp"] = self.dpname
	def sendInfo(self):
		return self.newUserInfo
	def submitDetails(self):
		self.getInfo()
		self.cc.new_user = self.newUserInfo
		self.cc.createUser()

class EditProfile(newAccountFrame):
	def setInfo(self, root, cc):
		self.root = root
		self.cc = cc
		self.label_1.configure(text="Edit Profile")
		self.usernameEntry.insert(0, self.cc.user.username)
		self.passwordEntry.insert(0, self.cc.user.password)
		self.firstnameEntry.insert(0, self.cc.user.firstname)
		self.lastnameEntry.insert(0, self.cc.user.lastname)
		self.genderEntry.insert(0, self.cc.user.gender)
		self.vardays.set(self.days[int(self.cc.user.birthdate)])
		self.varmonths.set(self.months[int(self.cc.user.birthmonth)])
		self.chooseyears.insert(0, self.cc.user.birthyear)
		self.eduHistoryEntry.insert(1.1, self.cc.user.eduHistory)
		self.jobHistoryEntry.insert(1.1, self.cc.user.jobHistory)
		self.dpname = self.cc.user.dp

class Profile:
	def __init__(self, root, cc):
		self.profile = _Profile(root, cc, cc.userinfo)

class _Profile:
	def __init__(self, root, cc, userinfo):
		self.profile = root
		self.cc = cc
		
		self.profile_details = Frame(self.profile)
		self.profile.grid()
		
		self.profile_side = Frame(self.profile)
		self.profile_side.place(x=0, y=0)
		
		self.ps = Canvas(self.profile_side, bg="light green")
		self.ps.pack(side=TOP, fill=BOTH)
		self.ps.configure(height=480, width=213)
		
		dp = PhotoImage(file=userinfo.get("dp"))
		dpLabel = Label(self.profile_side, image=dp, width=150, height=150)
		dpLabel.place(x=30, y=30)
		name = userinfo.get("firstname")+" "+userinfo.get("lastname")
		uname = Label(self.profile_side, text=name)
		gender = Label(self.profile_side, text=userinfo.get("gender"))
		uname.place(x=30, y=190)
		gender.place(x=30, y=210)
		
		self.post_part = Frame(self.profile)
		self.post_part.place(x=215, y=0)
		self.ss = Canvas(self.post_part, bg="light blue")
		self.ss.pack(side=TOP, fill=BOTH)
		self.ss.configure(height=110, width=420)
		label_1 = Label(self.ss, text="How are you?", bg="light blue")
		label_1.place(x=23, y=30)
		self.status = Entry(self.ss, width=63)
		self.status.place(x=23, y=50)
		post = Button(self.ss, text="Post", command=self.post)
		post.place(x=375, y=75)
		
		self.allStat = Frame(self.profile)
		self.allStat.place(x=215, y=113)
		self.stats = Canvas(self.allStat, bg="light blue", scrollregion=(0, 0, 370, 420))
		self.stats.pack(side=TOP, fill=BOTH)
		self.stats.configure(height=370, width=420)
		s = Scrollbar(self.allStat, orient=VERTICAL)
		s.pack(fill=Y, side=RIGHT)
		s.configure(command=self.stats.yview)
		self.stats.config(yscrollcommand=s.set)
		
		stats = self.cc._getAllStats(userinfo.get("username"))
		for status in stats:
			Label(self.stats, text=status).pack(side=TOP)
			Label(self.stats, text="\t"+stats.get(status)).pack(side=TOP)
	def post(self):
		status = self.status.get()
		self.cc.status = status
		self.cc.newStatus()
		
class Message:
	def __init__(self, root, cc):
		self.root = root
		self.cc = cc
		self.menu = Frame(self.root)
		self.menu.place(x=0, y=0)
		self.mess = Frame(self.root)
		self.mess.place(x=213, y=0)
		self.messC = Canvas(self.mess, bg="light green", height=480, width=427).pack(side=TOP, fill=BOTH)
		
		menuC = Canvas(self.menu, bg="light green", height=480, width=213).pack(side=TOP, fill=BOTH)
		newMess = Button(menuC, text="New Message", command=self.new).place(x=10, y=50)
		received = Button(menuC, text="Inbox", command=self.inbox).place(x=10, y=80)
		sent = Button(menuC, text="Outbox", command=self.outbox).place(x=10, y=110)
		
	def new(self):
		self.mess.destroy()
		self.mess = Frame(self.root)
		self.mess.place(x=213, y=0)
		self.messC = Canvas(self.mess, bg="light green", height=480, width=427).pack(side=TOP, fill=BOTH)
		label = Label(self.messC, text="temp").place(x=10, y=10)
	def inbox(self):
		self.mess.destroy()
		self.mess = Frame(self.root)
		self.mess.place(x=213, y=0)
		self.messC = Canvas(self.mess, bg="light green", height=480, width=427).pack(side=TOP, fill=BOTH)
		self.label = Label(self.messC, text="hey").place(x=10, y=10)
	def outbox(self):
		print "-"

class Friends:
	def __init__(self, root, cc):
		self.root = root
		self.cc = cc
		self.friends = Frame(self.root, bg="light green").place(x=0, y=0)
		friends_c = Canvas(self.friends, bg="white", scrollregion=(0, 0, 200, 350), height=350, width=200, bd=2, highlightbackground="Black").place(x=220, y=30)
		#y = Scrollbar(self.friends, command=friends_c.yview).grid(row=0, column=0, sticky=N+S)
		#friends_c["yscrollcommand"] = y
		self.friend_list = self.cc.getFriends()
		self.var = IntVar()
		self.friendbuttons = []
		_x=225
		_y=35
		i=0
		for friends in self.friend_list:
			self.friendbuttons.append(Radiobutton(friends_c, text=friends, variable=self.var, value=i, command=self.select))
			self.friendbuttons[-1].place(x=_x, y=_y)
			_y = _y+30
			i = i+1
		Button(friends_c, text="view", command=self.view).place(x=_x, y=_y+30)
	def select(self):
		self.friend_info = self.friend_list[self.var.get()]
	def view(self):
		self.friend_page = Frame(self.root)
		self.cc.getSearchInfo(self.friend_info)
		see_friend = _Profile(self.root, self.cc, self.cc.searchinfo)

class Search:
	def __init__(self, root, search, cc):
		self.search = search
		self.root = root
		self.cc = cc
		self.search.geometry("220x100")
		self.search.title("Search")
		self.username = Entry(self.search, width=32)
		self.username.place(x=10, y=10)
		Label(self.search, text="Type the username above").place(x=10, y=40)
		submit = Button(self.search, text="Search", command=self.submit).place(x=50, y=60)
	def submit(self):
		username = self.username.get()
		results = self.cc.searchUser(username)
		if results == True:
			self.other_profile = Frame(self.root)
			self.cc.getSearchInfo(username)
			searchProfile = _Profile(self.root, self.cc, self.cc.searchinfo)
			self.view(searchProfile)
			self.search.destroy()
		else:
			tkMessageBox.showinfo("search Results", "Username not found!")
	def view(self, profile):
		Button(profile.ps, text="Add", command=self.add).place(x=30, y=10)
	def add(self):
		print "-"
root = Tk()
start = MainMenu(root)
root.mainloop()
exit(0)
#Add friends
#Add medical info with link to how to solve the disease
#Add I don't have a pet option
#Add error check for the file selector if not an image
"""
Main file
"""

#import the needed packages
import functions, smtplib, password, sqlite3, os.path, os

#Set up the SQL database
db = sqlite3.connect('User.db')
cursor = db.cursor()
cursor.execute('''CREATE TABLE if not exists users (username text primary key, password text, email text, age text, petname text, bio text, todayDate text, filename text, career text, gender text, homeAddress text)''')
cursor.execute('''CREATE TABLE if not exists friends (user text primary key, friendsList text, friendRequests text)''')
db.commit()
db.close()

#Create variables
loggedin = False
RegisterRun = False
emailFound = False

#Create a navigational menu
exit  = False
while not exit:
	print('1. Register')
	if loggedin:
		print('2. Log out')
		print('3. Exit')	
	else:
		print('2. Login')
		print('3. Exit')
	selection = input('Input: ')
	if selection == '1':
		#Register
		os.system('clear')
		functions.Register()
	if loggedin:
		if selection == '2':
			#Log Out
			os.system('clear')
			loggedin = functions.LogOut(UsernameLogin)
		elif selection == '3':
			#Exit
			os.system('clear')
			exit = True
	else: 
		if selection == '2':
			#Login
			UsernameLogin, loggedin = functions.Login()
		elif selection == '3':
			#Exit
			os.system('clear')
			exit = True




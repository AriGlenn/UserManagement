import os.path, os
os.system('clear')
import smtplib, getpass, datetime, time, random, webbrowser, password, sqlite3, googlemaps
from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from twilio.rest import TwilioRestClient
import functions


print('Loading...')
#Set up SQL
db = sqlite3.connect('User.db')
cursor = db.cursor()
cursor.execute('''CREATE TABLE if not exists users (username text primary key, password text, email text, age text, petname text, bio text, todayDate text, filename text, career text, gender text, homeAddress text)''')
cursor.execute('''CREATE TABLE if not exists friends (user text primary key, friendsList text, friendRequests text)''')
db.commit()
db.close()


#Set up Email server
try:
	server = smtplib.SMTP('smtp.gmail.com', 587) #port 465 or 587
	server.ehlo()
	server.starttls()
	server.ehlo()
	server.login(password.password3, password.password2)
except:
	print('It seems something went wrong, please check your wifi connectivity and try again')
	quit()

	
#Create variables
loggedin = False
RegisterRun = False
emailFound = False


"""
Add friends
Add medical info with link to how to solve the disease
Add I don't have a pet option
Add telephone number
Add error check for the file selector if not an image
add squl to readme
"""



#Create a navigational menu
exit  = False
while not exit:
	#os.system('clear')
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
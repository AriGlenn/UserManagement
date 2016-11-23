
import smtplib, os.path, os
os.system('clear')
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


loggedin = False
RegisterRun = False
emailFound = False
accounts = []
if not os.path.isfile('accounts.txt'):
	print('Creating accounts.txt ...')
	open('accounts.txt', 'w')

with open('accounts.txt', 'r') as myFile:
	info = myFile.read()
	info = info.split(',')
	for i in range(len(info)):
		if i%5 == 0:
			accounts.append(info[i:i+5])
"""
	add Security questions
		#Please enter the name of your first pet
	change encryption of pass to include numbers
	add back function when Registering
"""

def askQuestion():
	print('Username and Passwords must only contain letters and numbers')
	Username = input('Create a Username: ')
	Password = input('Create a Password: ')
	CheckPassword = input('Please re-type your Password: ')
	if CheckPassword != Password:
		print('Error: Not the same password' + '\n' + 'Please Try Again'  + '\n')
	emailAddress = input ('Please enter a recovery email: ')
	birthday = input('Please enter the year you were born: ')
	petname = input('Please enter your first pet\'s name: ')
	for account in accounts:
		if account[0] == Username:
			print('This username has already been taken.')
			askQuestion()
	if Username == '' or Password == '' or emailAddress == '' or birthday == '' or petname == '':
		print('Error: You have left one of the questions blank')
		askQuestion()

	if '@' not in emailAddress or '.' not in email:
		print('Error: The email adress you have typed in does not exist. Please try again.')
		askQuestion()

	#ENCRYPT THE PASSWORD	
	key = 'badcfehgjilknmporqtsvuxwzy '
	alphabet = 'abcdefghijklmnopqrstuvwxyz '
	Password = Password.lower()
	encryptedPassword = ''
	for ch in Password:
		index = alphabet.find(ch)
		encryptedPassword += key[index]

	try:
		int(birthday)
	except ValueError:
		print('Error: You typed in a word instead of a number for your birthday')
		askQuestion()
	else:
		return Username, encryptedPassword, emailAddress, birthday, petname

def Register():
	Username, encryptedPassword, emailAddress, birthday, petname = askQuestion()
	calculatedAge = 2016 - int(birthday)
	with open('accounts.txt', 'a') as myFile:
		myFile.write(str(Username) + ',' + str(encryptedPassword) + ',' + str(calculatedAge) + ',' + str(petname) + ',' + str(emailAddress) + ',')
	with open('accounts.txt', 'r') as myFile:
		info = myFile.read()
		info = info.split(',')
		for i in range(len(info)):
			if i%5 == 0:
				accounts.append(info[i:i+5])
	print('\n' + Username + '\'s account has been made. \n')

def Login():
	emailFound = False
	UsernameLogin = input('Enter a Username: ')
	PasswordLogin = input('Enter a Password: ')

	key = 'badcfehgjilknmporqtsvuxwzy '
	alphabet = 'abcdefghijklmnopqrstuvwxyz '
	PasswordLogin = PasswordLogin.lower()
	encryptedLoginPassword = ''
	for ch in PasswordLogin:
		index = alphabet.find(ch)
		encryptedLoginPassword += key[index]
	
	for account in accounts:
		if account[0] == UsernameLogin and account[1] == encryptedLoginPassword:
			loggedin = True
			age = account[2]
			petname = account[3]
			print('Welcome user ' + UsernameLogin + '!')
			print('You are ' + age + ' years old.')
			print('You\'re first pet\'s name is ' + petname + '.')
	global loggedin
	if not loggedin:
		print('Incorrect password or username: Please Try Again')
		reset = input('Forgot Password? Press 1 to reset: ')
		if reset == '1':
			resetUsername = input('Enter your username associated with the account you would like to recovery: ')
			for account in accounts:
				if account[0] == UsernameLogin:
					resetPassword = account[1]
					resetEmail = account[4]

					key = 'badcfehgjilknmporqtsvuxwzy '
					alphabet = 'abcdefghijklmnopqrstuvwxyz '
					resetPasswordDecrypted = ''
					for ch in resetPassword:
						index = key.find(ch)
						resetPasswordDecrypted += alphabet[index]

					message = '\n\nRecovery account_info: \nHello ' + resetUsername + ',\n' + 'Your Password is ' + resetPasswordDecrypted + '\n \n Thanks for your service \n -Recovery Accounts.info'
					print(message)
					server.sendmail('InfoRecovery.User@gmail.com', resetEmail, message)
					print('You will be receiveing an email shortly...')
					emailFound = True
			if emailFound == False:
				print('The username you typed in does not exist.')
	return UsernameLogin, loggedin

def LogOut(UsernameLogin):
	loggedin = False
	print(UsernameLogin + ' has logged out --  ')
	return loggedin


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



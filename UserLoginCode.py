

import smtplib
import os.path

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

RegisterRun = False

accounts = []
with open('accounts.txt', 'r') as myFile:
	info = myFile.read()
	info = info.split(',')
	for i in range(len(info)):
		if i%5 == 0:
			accounts.append(info[i:i+5])
	print(accounts)

loggedin = False


"""
-add readme File
-add LogOut where you can only log out once logged in
-add func of if someone wans to recover account, but the account does not exist
-add username is already taken

EXTRA:
	add encrypted password
	add Security questions
		#Please enter the name of your first pet
"""

def askQuestion():
	print('Username and Passwords must only contain letters and number')
	Username = input('Create a Username: ')
	Password = input('Create a Password: ')
	CheckPassword = input('Please re-type your Password: ')
	if CheckPassword != Password:
		print('Error: Not the same password' + '\n' + 'Please Try Again'  + '\n')
	receiver = input ('Please enter a recovery email: ')
	birthday = input('Please enter the year you were born: ')
	petname = input('Please enter your first pet\'s name: ')
	
	if Username == '' or Password == '' or receiver == '' or birthday == '' or petname == '':
		print('Error: You have left one of the questions blank')
		askQuestion()
	try:
		int(birthday)
	except ValueError:
		print('Error: You typed in a word instead of a number for your birthday')
		askQuestion()
	else:
		return Username, Password, receiver, birthday, petname

def Register():

	Username, Password, receiver, birthday, petname = askQuestion()
	calculatedAge = 2016 - int(birthday)
	with open('accounts.txt', 'a') as myFile:
		myFile.write(str(Username) + ',' + str(Password) + ',' + str(calculatedAge) + ',' + str(petname) + ',' + str(receiver) + ',')
	
	




def Login():
	emailFound = False
	UsernameLogin = input('Enter a Username: ')
	PasswordLogin = input('Enter a Password: ')
	for account in accounts:
		if account[0] == UsernameLogin and account[1] == PasswordLogin:
			loggedin = True
			age = account[2]
			petname = account[3]
	if loggedin:
		print('Welcome user ' + UsernameLogin + '!')
		print('You are ' + age + ' years old.')
		print('You\'re first pet\'s name is ' + petname + '.')
	else:
		print('Incorrect password or username: Please Try Again')
		reset = input('Forgot Password? Press 1 to reset: ')
		if reset == '1':
			resetUsername = input('Enter your username associated with the account you would like to recovery: ')
			for account in accounts:
				if account[0] == UsernameLogin:
					resetPassword = account[1]
					resetEmail = account[4]
					message = 'Hello ' + resetUsername + '\n' + 'Your Password is ' + resetPassword
					server.sendmail('InfoRecovery.User@gmail.com', resetEmail, message)
			print('You will be receiveing an email shortly...')
	return UsernameLogin



def LogOut(UsernameLogin):

	loggedin = False
	print(UsernameLogin + ' has logged out --  ')
#	print(Username + ' has logged out')


exit  = False
while not exit:
	print('1. Register')
	print('2. Login')
	print('3. Log out')
	print('4. Exit')
	selection = input('Input: ')

	if selection == '1':
		#Register
		Register()

	elif selection == '2':
		#Login
		UsernameLogin = Login()
		
	elif selection == '3':
		#Log Out
		LogOut(UsernameLogin)


	elif selection == '4':
		exit = True


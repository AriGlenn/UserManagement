

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


"""
-add readme File

-bug of not registering the sign in

EXTRA:

	add encrypted password

	add age , pets name

	add Security questions
		#Please enter the name of your first pet

"""


def Register():
	print('Username and Passwords must only contain letters and number')
	Username = input('Create a Username: ')
	Password = input('Create a Password: ')
	CheckPassword = input('Please re-type your Password: ')
	if CheckPassword != Password:
		print('Error: Not the same password' + '\n' + 'Please Try Again'  + '\n')
	receiver = input ('Please enter a recovery email: ')
	birthday = input('Please enter the year you were born: ')
	petname = input('Please enter your first pet\'s name : ')
	calculatedAge = 2016 - int(birthday)
	
	with open('accounts.txt', 'a') as myFile:
		myFile.write(str(Username) + ' ' + str(Password) + ' ' + str(calculatedAge) + ' ' + str(petname) + '\n')
	with open('accounts.txt', 'a') as myFile:
		myFile.write('True' + '\n')
	return Username, Password
	
	




def Login(Username, Password):
	
	loggedin = False
	UsernameLogin = input('Enter a Username: ')
	PasswordLogin = input('Enter a Password: ')
	accounts = open('accounts.txt', 'r')
	accounts = accounts.read()
	accounts = accounts.split()
	for x in range(int(len(accounts))):
		if accounts[x] == UsernameLogin and accounts[x+1] == PasswordLogin:
			loggedin = True
			age = accounts[x+2]
			petname = accounts[x+3]

	if loggedin == True:
		print('Welcome user ' + UsernameLogin + '!')
		print('You are ' + age + ' years old.')
		print('You\'re first pet\'s name is ' + petname + '.')



	else:
		print('Incorrect password or username: Please Try Again')
		reset = input('Forgot Password? Press 1 to reset: ')
		if reset == '1':
			receiver = input('Enter your recovery email: ')
			message = 'This is a recovery email'
			message = 'Your Username is ' + Username + '\n' + 'Your Password is ' + Password
			server.sendmail('InfoRecovery.User@gmail.com', receiver, message)
			print('You will be receiveing an email shortly...')


def LogOut():

		loggedin = False
		print(Username + ' has logged out')


exit  = False
while not exit:
	print('1. Register')
	print('2. Login')
	print('3. Log out')
	print('4. Exit')
	selection = input('Input: ')

	if selection == '1':
		#Register
		Username, Password = Register()

	elif selection == '2':
		#Login
		accounts = open('accounts.txt', 'r')
		accounts = accounts.read()
		accounts = accounts.split()
		for x in range(int(len(accounts)/2)):
			if accounts[x] == 'True':
				Login(Username, Password)
		
	elif selection == '3':
		#Log Out
		if loggedin == True:
			LogOut()


	elif selection == '4':
		exit = True


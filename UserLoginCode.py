

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
add readme myFile

add logout file

add encrypted password

add text file to store email

add string substitution template 

add bio (extra info)

fix bugs on line 70 and 79

"""


def Register():
	print('Username and Passwords must only contain letters and number')
	Register.Username = input('Create a Username: ')
	Register.Password = input('Create a Password: ')
	CheckPassword = input('Please re-type your Password: ')
	receiver = input ('Please enter a recovery email: ')
	if CheckPassword != Password:
		print('Error: Not the same password' + '\n' + 'Please Try Again'  + '\n')
	with open('accounts.txt', 'a') as myFile:
		myFile.write(str(Username) + ' ' + str(Password) + '\n')
	with open('accounts.txt', 'a') as myFile:
		myFile.write('True' + '\n')



def Login():
	
	loggedin = False
	UsernameLogin = input('Enter a Username: ')
	PasswordLogin = input('Enter a Password: ')
	accounts = open('accounts.txt', 'r')
	accounts = accounts.read()
	accounts = accounts.split()
	for x in range(int(len(accounts)/2)):
		if accounts[x] == UsernameLogin and accounts[x+1] == PasswordLogin:
			loggedin = True
	if loggedin == True:
		print('Welcome user ' + UsernameLogin + '!')
	else:
		print('Incorrect password or username: Please Try Again')
		reset = input('Forgot Password? Press 1 to reset: ')
		if reset == '1':
			receiver = input('Enter your recovery email: ')
#			message = 'Your Username is ' + Register.Username + '\n' + 'Your Password is ' + Register.Password
			server.sendmail('InfoRecovery.User@gmail.com', receiver, message)
			print('You will be receiveing an email shortly...')


def LogOut():

		loggedin = False
#		print(userLogOut + ' has logged out')


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
		accounts = open('accounts.txt', 'r')
		accounts = accounts.read()
		accounts = accounts.split()
		for x in range(int(len(accounts)/2)):
			if accounts[x] == 'True':
				Login()
		
	elif selection == '3':
		#Log Out
		if loggedin == True:
			LogOut()


	elif selection == '4':
		exit = True


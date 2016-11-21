


def Register():
	print('Username and Passwords must only contain letters and number')
	Username = input('Create a Username: ')
	Password = input('Create a Password: ')
	CheckPassword = input('Please re-type your Password: ')

	if CheckPassword != Password:
		print('Error: Not the same password' + '\n' + 'Please Try Again'  + '\n')

	with open('accounts.txt', 'w') as myFile:
		myFile.write(str(Username) + ' ' + str(Password) + '\n')





def Login():
	UsernameLogin = input('Enter a Username: ')
	PasswordLogin = input('Enter a Password: ')


def LogOut():
	pass


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
 		Login()
	
	elif selection == '3':
		#Log Out
		LogOut()


	elif selection == '4':
		exit = True


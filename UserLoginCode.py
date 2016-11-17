





def Register():
	pass

def Login():
	pass

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


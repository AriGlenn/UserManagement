# User Management

## How it works
This program can register, login, and logout of any account. The accounts are stored and can be used after the program is closed and re-opened. The program has a recovery email, where if you forget your password or username, it will send you an emial containg the information. This program stores your age, first pet's name, and much more. 


## The code
#### Store the username, password, age, and first pet's name
```
with open('accounts.txt', 'a') as myFile:
		myFile.write(str(Username) + ' ' + str(Password) + ' ' + str(calculatedAge) + ' ' + str(petname) + '\n')
```

#### Create a main menu
```
exit  = False
while not exit:
	print('1. Register')
	print('2. Login')
	print('3. Log out')
	print('4. Exit')
	selection = input('Input: ')
```

#### Set up a server to deliver a recovery email
```
import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587) #port 465 or 587
server.ehlo()
server.starttls()
server.ehlo()
server.login('InfoRecovery.User@gmail.com','Recovery36')

#If the account needs to be recovered, and to send the email
receiver = input('Enter your recovery email: ')
message = 'Your Username is ' + Username + '\n' + 'Your Password is ' + Password
server.sendmail('InfoRecovery.User@gmail.com', receiver, message)
print('You will be receiveing an email shortly...')
```

#### Create a navigation menu once logged in
Once the user has logged in:
```
if loggedin == True:
		print('Welcome user ' + UsernameLogin + '!')
		print('You are ' + age ' years old.')
		print('You\'re first pet\'s name is ' + petname + '.')
```

#### To make sure the password has been typed in correctly
```
print('Username and Passwords must only contain letters and number')
Username = input('Create a Username: ')
Password = input('Create a Password: ')
CheckPassword = input('Please re-type your Password: ')
    
if CheckPassword != Password:
		print('Error: Not the same password' + '\n' + 'Please Try Again'  + '\n')
```

By: Ari Glenn

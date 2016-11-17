# User Management

## Challenge
For this challenge, you need to create a user management system.
That is, a program that allows a user to register an account,
login with a username and password, and logout.

## Extra Challenges
The following suggestions are extra challenges to make your program
more sophisticated.

#### Password Reset
Implement password reset functionality so that if a user forgets
their password, their account can be recovered.

#### Profile Data
Include extra user data, beyond a username and password, in the
registration process. Then make a simple profile page for displaying
that info.

#### Data Storage
Instead of storing a plain text file, use a json file, or use a
database such as sqlite or MongoDB.

## Code
Code snippets and hints that might be useful

#### Open a file for writing
```python
with open('numbers.txt', 'w') as myFile:

    for x in range(10):
        myFile.write('line: ' + str(x) + '\n') #newline character is necessary.
```

#### Open a file for reading
```python
with open('someFile.txt', 'w') as myFile: #someFile.txt must exist

    for x in myFile.readlines():
        print(x)
```

#### Split a line of text
```python
>>> line = "Martha Stewart, 75, NJ"
>>> line.split()
['Martha', 'Stewart,', '75,', 'NJ']
>>> line.split(",")
['Martha Stewart', ' 75', ' NJ']
>>> myList = line.split(",")
>>> myList[1]
' 75'
>>>
```

#### Create a navigation prompt
```python
exit = False

while not exit:

    print('1. Stuff')
    print('2. Other Stuff')
    print('3. Different Stuff')
    print('4. Exit')

    s = input('Make a selection: ')

    if s == '4':
        exit = True
```

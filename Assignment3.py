import re

pwLen = re.compile(r'.{8,}')
pwUpper = re.compile(r'[A-Z]+')
pwLower = re.compile(r'[a-z]+')
pwNum = re.compile(r'[0-9]+')
pwSym = re.compile(r'[!@#$%*&]+')

print('Password requirements: \nmust be at least 8 characters long, \nmust have an at least one uppercase letter, \nmust have a least one lower case letter, \nmust have at least one number, \nand must have at least one symbol')
password = input('Please enter what you want your password to be: ')

    
while True:
    while pwLen.search(password) is None:
        print('Your password needs to be at least 8 characters long')
        break
    while pwUpper.search(password) is None:
        print("Your password needs at least one upper case letter")
        break
    while pwLower.search(password) is None:
        print('Your passowrd needs at least one lower letter')
        break
    while pwNum.search(password) is None:
        print('Your password needs at least one number')
        break
    while pwSym.search(password) is None:
        print('Your password needs at least one symbol')
        break
    else:
        print('Your password is good')
    break
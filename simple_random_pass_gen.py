# This is only a simple random password generator :)

import random

# https://stackoverflow.com/questions/287871/how-to-print-colored-text-to-the-terminal

OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
ENDC = '\033[0m'

letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "123456789"
symbols = "$#%^&*(){}[];/!:;''\""

passLen = 0
while passLen < 8:
	try:
		passLen = int(input(OKBLUE + "Password length (min=8):" + ENDC + " "))
	except:
		print(WARNING + "\tPlease input only numbers\n" + ENDC)

n = 0
password = ''
while n < passLen:
	let = letters[random.randint(0, len(letters) - 1)]
	num = numbers[random.randint(0, len(numbers) - 1)]
	sym = symbols[random.randint(0, len(symbols) - 1)]
	if random.randint(0, 3) == 0:
		password += num
	elif random.randint(3, 6) == 4:
		password += sym
	else:
		password += let
	n += 1


print("\n" + OKGREEN + password + ENDC)

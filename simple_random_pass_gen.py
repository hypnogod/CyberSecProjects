# This is only a simple random password generator :)

import random

letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "123456789"
symbols = "$#%^&*(){}[];/!:;''\""

passLen = 0
while passLen < 8:
	try:
		passLen = int(input("password length (min=8): "))
	except:
		print("Please input only numbers")

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

print(password)

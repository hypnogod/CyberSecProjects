import re
quit = False # default value

def shiftAlgo(case, s, c):
	f = ''
	if case == "lower":
		# 97 = a
		f += chr(97 + (ord(c) - 97 + s)%26)
	elif case == "upper":
		# 65 = A
		f += chr(65 + (ord(c) - 65 + s)%26)
	return f

def cesarcipher(a, shift, ap):
	final = ''
	for i in range(len(a)):
		# get a single character from cipher
		char = a[i:i+1]
		# check if the "cipher" is aphabet or not
		if char.isalpha() or char == ' ':
			# lower and upper cipher text have diffrent algorithm
			if char.islower():
				final += shiftAlgo("lower", shift, char)
			elif char.isupper():
				final += shiftAlgo("upper", shift, char)
			else:
				final += ' '
		else:
			print("\n{} is not in expected list:\n{}".format(char, ap))
			global quit
			quit = True
	return final


Alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
plaintext = input("Caesar code plain text: ") # get plaintext
plaintext = re.sub(r"[\n\t\s]", " ", plaintext) # replace spaces
automode = str(input("Test all possible shifts (y/n): ")) # brute force?

if automode == 'y':
	for i in range(1, 26 + 1):
		print("+{}".format(i), cesarcipher(plaintext, i, Alphabets))
		if quit:
			break
elif automode == 'n':
	shift = int(input("The Shift (number): "))
	while shift > 26 or shift < 0:
		shift = int(input("Please try again: "))

	print("\n",cesarcipher(plaintext, shift, Alphabets))
else:
	print("Please try again")

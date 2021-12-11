import re
from pyfiglet import figlet_format

quit = False

print(figlet_format("Cesar Cipher"))

def decodeCesarCipher(cipher, key):
	result = ''
	temp = ''
	for c in cipher:
		if c.isalpha():
			if c.islower():
				if ((ord(c) - 97 - key) < 0):
					temp = 97 + ((ord(c) - 97 - key + 26) % 26) 
				else:
					temp = 97 + ((ord(c) - 97 - key) % 26) 
				result += chr(temp)
			elif c.isupper():
				if ((ord(c) - 65 - key) < 0):
					temp = 65 + ((ord(c) - 65 - key + 26) % 26) 
				else:
					temp = 65 + ((ord(c) - 65 - key) % 26) 
				result += chr(temp)
		else:
			result += c
	return result
	
# Encode
def cesarcipher(a, s):
	# a = plaintext
	# s = shift
	Alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	final = ''
	for i in a:
		# get a single character from cipher
		# check if the "cipher" is aphabet or not
		if i.isalpha() or i == ' ':
			# lower and upper cipher text have diffrent algorithm
			if i.islower():
				final += chr(97 + (ord(i) - 97 + s)%26)
			elif i.isupper():
				final += chr(65 + (ord(i) - 65 + s)%26)
			else:
				final += ' '
		else:
			print("\n{} is not in expected list:\n{}".format(i, Alphabets))
	return final

# Start Enc Function
def startEncProcess():
	plaintext = input("Caesar code plain text: ")
	plaintext = re.sub(r"[\n\t\s]", " ", plaintext)
	shift = int(input("The Shift (number): "))
	while shift > 26 or shift < 0:
		shift = int(input("Please try again: "))
	enctxt = cesarcipher(plaintext, shift)
	print("\nThe encoded message is:\n" + enctxt)

def startDecProcess():
	ciphertext = input("Caesar shifted ciphertext: ")
	ciphertext = re.sub(r"[\n\t\s]", " ", ciphertext)
	automode = str(input("Test all possible shifts (y/n): "))
	if automode == 'y':
		for i in range(1, 26 + 1):
			print("+{}".format(i),decodeCesarCipher(ciphertext, i))
			if quit:
				break;
	elif automode == 'n':
		key = int(input("Enter you key/shift (number): "))
		while key > 26 or key < 0:
			key = int(input("Please try again: "))
		print("\n",decodeCesarCipher(ciphertext, key))
	else:
		print("Please try again!")


	

running = True
while running:
	option = str(input("\nChoose (e) for encrypt and (d) for decrypt: ")).lower()
	if option == "e":
		print("\n", "-" * 20, "Encryption", "-"*20, "\n")
		startEncProcess()
		running = False
	elif option == "d":
		print("\n", "-" * 20, "Decrypt", "-"*20, "\n")
		startDecProcess()
		running = False
	else:
		print("\n\tPlease try again")

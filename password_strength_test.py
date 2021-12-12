import re
import time

# https://www.geeksforgeeks.org/print-colors-python-terminal/#main
def prGreen(skk): print("\033[92m{}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m\n","-"*20,"{}" .format(skk), "-"*20, "\n\033[00m")




prCyan("Password Strength Test")

user_pass = str(input("\033[93mCheck your password: \033[00m"))

score = 0

LENGTH_CHECK = len(user_pass) >= 12
LOWERCASE_CHECK = bool(re.search('[a-z]+', user_pass))
NUMBER_CHECK = bool(re.search('[0-9]+', user_pass))
UPPERCASE_CHECK = bool(re.search('[A-Z]+', user_pass))
SYMBOLS_CHECK = bool(re.search("[@_!#$%^&*()<>?/|}{~:+-]", user_pass))

if not LENGTH_CHECK:
	print("\n- Password should be 12 characters or higher")
	time.sleep(0.5)
if not LOWERCASE_CHECK:
	print("\n- Your Password should contain at least one lower case character.")
	time.sleep(0.5)
if not UPPERCASE_CHECK:
	print("\n- Your Password should contain at least one upper case character.")
	time.sleep(0.5)
if not NUMBER_CHECK:
	print("\n- Your Password should contain at least one number.")
	time.sleep(0.5)

if not SYMBOLS_CHECK:
	print("\n- Your password should contain at least one symbol.")
	time.sleep(0.5)

perfectPASS = LENGTH_CHECK and LOWERCASE_CHECK and UPPERCASE_CHECK and NUMBER_CHECK and SYMBOLS_CHECK

if perfectPASS:
	prGreen("\nYour Password Meets All Requirements\n")

# Tips 
prCyan("Tips")
print("\n- Hard time remembering complex passwords? Use passphrase.")
time.sleep(0.5)
print("\n- Only change passwords, if you are concerned they may have been compromised.")
time.sleep(0.5)
print("\n- Have unique password for all accounts.")
time.sleep(0.5)
print("\n- Use password managers to store yours unique passwords.")
time.sleep(0.5)
print("\n- Use Multi-factor Authentication whenever possible.")


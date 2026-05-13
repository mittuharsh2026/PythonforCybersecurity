import random
import string

print("Password Generator")

length = int(input("Password length 4-300: "))
length = max(4, min(length, 300))

chars = ""

if input("Use lowercase? y/n: ") == "y":
    chars += string.ascii_lowercase
if input("Use uppercase? y/n: ") == "y":
    chars += string.ascii_uppercase
if input("Use numbers? y/n: ") == "y":
    chars += string.digits
if input("Use symbols? y/n: ") == "y":
    chars += "!@#$%^&*"

if chars == "":
    chars = string.ascii_letters + string.digits

amount = int(input("How many passwords? "))

for i in range(amount):
    password = ""
    for j in range(length):
        password += random.choice(chars)
    print(password)

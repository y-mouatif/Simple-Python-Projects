#import random
import random

#creating the components of the password generator
upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowerCase = upperCase.lower()
digits = "0123456789"
symbols = "!@#$%?&*()/&+-_="

#creating boolean variables to select the components of the password and initially setting them to false
upper, lower, nums, syms = False, False, False, False

# asking the user which components they want in their password
print("Welcome to the password generator!")
print("Select the components you want in your password:")
if input("Uppercase letters? (y/n): ").lower() == "y":
    upper = True
if input("Lowercase letters? (y/n): ").lower() == "y":
    lower = True
if input("Digits? (y/n): ").lower() == "y":
    nums = True
if input("Symbols? (y/n): ").lower() == "y":
    syms = True

passw = ""

if upper:
    passw += upperCase
if lower:
    passw += lowerCase
if nums:
    passw += digits
if syms:
    passw += symbols

# asking the user for the length and amount of passwords they want
length = int(input("Enter the length of the password(s): "))
amount = int(input("Enter the amount of passwords you want: "))

# generating the passwords and printing them
print("\nHere are your passwords:")
for x in range(amount):
    password = "".join(random.sample(passw, length))#we are taking random samples of length "length" from passw
    print(password)

    
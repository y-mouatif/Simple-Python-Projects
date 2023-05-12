

# import random
import random

# randint() will generate a random integer between 1-50
number = random.randint(1,50)

# guess will store the guesses that the user makes
guess = 0

# while loop to continue the game until the user guesses correctly
while guess != number:
  
  # prompt the user to enter a guess, the input() function will return the 
  #  convert the input to an int with int() and assign the 
  # guess to 'user_guess'
  user_guess = int(input("Enter your guess from 1 to 50: "))
  
  # if the user guesses too lower, tell them to guess higher, if they guess 
  # too high, tell them to guess lower, and if they get it correct tell 
  # them they've won
  if (user_guess < number):
    print("Guess higher!")
  elif (user_guess > number):
    print("Guess lower!")
  else:
    print("You won!")
    quit()
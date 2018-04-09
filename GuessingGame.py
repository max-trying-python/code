import random

# generate random number
num = random.randrange(1, 21)
# if the user guessed the number right
guessed = False

for i in range(0, 5):
    guess = int(input("Guess the number!\n> "))

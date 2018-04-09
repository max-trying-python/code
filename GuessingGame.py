import random

# generate random number
num = random.randrange(1, 21)
# if the user guessed the number right
guessed = False

# repeat for 5 times
for i in range(0, 5):
    guess = int(input("Guess the number!\n> "))

    # too high
    if guess > num:
        print("You guessed too high!")
    # too low
    elif guess < num:
        print("You guessed too low!")
    # otherwise must be just right
    else:
        print("YOU WIN!")
        guessed = True
        break


# if the user hasn't guessed in time
if not guessed:
    print("\nYou used up your 5 guesses!")

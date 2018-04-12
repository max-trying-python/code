# read wordlist
wordsF = open("words.txt")

words = wordsF.read().split("\n")


# is the word valid?
def isInWord(word):
    if len(word) < 2:
        return False
    return word in words


# main loop
while True:
    word = input("Enter a word > ")

    # is it correct?
    if isInWord(word):
        print("Nice! \"{}\" is a valid Scrabble word!".format(word))

        choice = input("Would you like to try again (y/N)? [y] ")

        # do you want to continue?
        if choice.lower() == "y" or choice == "":
            pass
        else:
            print("Bye!")
            break

    else:
        choice = input("Not a valid Scrabble word! Would you like to try again (y/N)? [y] ")

        # do you want to continue?
        if choice.lower() == "y" or choice == "":
            pass
        else:
            print("Bye!")
            break

# constant words
words = ["mummy", "werewolf", "disguise", "graveyard", "cackle", "cobweb", "dracula", "ghostly", "mischief", "panic"]

# add spaces in the words
words = [" ".join(list(word)) for word in words]

# read the werewolf file
wordLines = open("werewolf.txt").read().split("\n")


# capitalize the words in a line
def capitalizeLine(line):
    for word in words:
        # capitalize the word if we find it
        line = line.replace(word, str.upper(word))
    return line


# LIST COMPREHENSION FTW!!!
wordLines = [capitalizeLine(line) for line in wordLines]

# print the lines
print("\n".join(wordLines))

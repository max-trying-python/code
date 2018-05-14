# constant words
words = ["mummy", "werewolf", "disguise", "graveyard", "cackle", "cobweb", "dracula", "ghostly", "mischief", "panic"]

# read the werewolf file
wordLines = open("werewolf.txt").read().split("\n")

newWords = [str.upper(line) for line in wordLines]

print(newWords)

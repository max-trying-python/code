# loop 5 times
for i in range(0, 5):
    print(("X " * 5).strip(), "\n")

# loop 10 times
for i in range(0, 11):
    # make a list from 0 to i, replace ints with strings, then join it with spaces
    print(" ".join(map(str, range(0, i))))

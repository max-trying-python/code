# imports
import time

# constant strings
str1 = " no no he's not dead, he's restin'! Remarkable bird, the Norwegian Blue, idn'it, ay? Beautiful plumage! "
str2 = " I took the liberty of examining that parrot when I got it home, and I discovered the only reason that it had been sitting on its perch in the first place was that it had been NAILED there."


# main bird function
def doStr(string):
    # 1. count the es
    time.sleep(0.5)
    print("1. Number of \"e\"s: " + str(string.count("e")))

    # 2. look for strings
    time.sleep(0.5)
    if string.find("dead") > -1 and string.find("bird") > -1:
        print("2. Found: dead bird")
    if string.find("parrot") > -1 and string.find("perch") > -1:
        print("2. Found: parrot perch")

    # 3. replacement
    time.sleep(0.5)
    print("3. Replaced: " + string.replace("Blue", "Lavender").replace("perch", "sofa"))

    # 4. Look for more strings
    time.sleep(0.5)
    if string.find("Norwegian") > -1:
        word = "Norwegian"
        for i in word:
            print("4. Letter is: " + i)

    # 5. find nailed
    if string.find("NAILED") > -1:
        print("5. Found nailed: " + string)


print("\n\nString 1:")
doStr(str1)

print("\n\nString 2:")
doStr(str2)

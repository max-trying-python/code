# ADD COMMENTS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# imports
import time

# constant strings
str1 = " no no he's not dead, he's restin'! Remarkable bird, the Norwegian Blue, idn'it, ay? Beautiful plumage! "
str2 = " I took the liberty of examining that parrot when I got it home, and I discovered the only reason that it had been sitting on its perch in the first place was that it had been NAILED there."


def doStr(string):
    time.sleep(0.5)
    print("Number of \"e\"s: " + str(string.count("e")))
    time.sleep(0.5)
    print("Replaced: " + string.replace("Blue", "Lavender").replace("perch", "sofa"))
    time.sleep(0.5)
    if string.find("dead") > -1 and string.find("bird") > -1:
        print("Found: dead bird")
    if string.find("parrot") > -1 and string.find("perch") > -1:
        print("Found: parrot perch")

    time.sleep(0.5)
    if string.find("Norwegian") > -1:
        word = "Norwegian"
        for i in word:
            print("Letter is: " + i)
    if string.find("NAILED") > -1:
        print("Found nailed: " + string)


print("\n\nString 1:")
doStr(str1)
print("\n\nString 2:")
doStr(str2)

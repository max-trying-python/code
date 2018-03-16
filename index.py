print("Hello, World!")

name = input("What's your name?\n")

chars = set('0123456789')

if name == "":
    print("I SAID TELL ME YOUR NAME DANGIT GO AWAY IM DONE WITH YOU")
    exit(1)
elif any((c in chars) for c in name):
    print("What idiot has a NUMBER in their freakin name?")
elif name.count(" ") < 1:
    print("Full name plz")
else:
    print("Oh hello there, " + name + "!")

# get input name
name = input("What's your first name?\n")+" "+input("What's your last name?\n")

# welcome them to give them a false sense of security so they give out personal info
print("Welcome, " + name)

# then ask them for personal info
age = input("What's your age?\n")
comment = ""

try:
    intAge = int(age)
except Exception as e:
    print("INVALID AGE")
    exit()

# mean comments based on age
if intAge > 100:
    comment = "Are you dead yet?"
elif intAge > 60:
    comment = "Have you retired yet?"
elif intAge > 25:
    comment = "Do you have a job yet?"
elif intAge > 18:
    comment = "Have you graduated yet?"
elif intAge > 6:
    comment = "Have you studied for your test yet?"
else:
    comment = "You're good at reading!"

# print the age
print("Your age is " + age + ". " + comment)

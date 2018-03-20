# get hours worked
hours = int(input("How many hours did you work this week?\n"))
# get money per hour
rawRate = input("How much money, in dollars, are you paid?\n").replace("$", "")
rate = int(rawRate)

rawTax = input("How much is tax in percent? (20%)\n")
tax = int(rawTax)

# calculate gross tax
gross = hours * rate
print("Your gross income (before tax): " + str(gross))

# calculate tax deduction
tax = gross * tax
print("Your tax: " + str(tax))

net = gross - tax
print("Your net income (after tax): " + str(net))

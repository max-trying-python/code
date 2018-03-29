# # # calculate overtime pay

# # constants
# how much overtime is multiplied by
overtime_multiplier = 1.5
# money earned per hour in dollars
money_per_hour = 10
# the most hours you can work WITHOUT GOING INTO OVERTIME
min_overtime_hours = 40

hours_worked = None
pay = None
try:
    hours_worked = float(input("How many hours did you work? "))
except Exception as e:
    print("You're supposed to give a number you idiot ")
    exit()
if hours_worked <= min_overtime_hours:
    msg = "No overtime pay! You didn't work for more than {} hours! ".format(min_overtime_hours)
    print(msg)
    pay = money_per_hour * hours_worked
elif hours_worked == 0:
    print("You can't work for no hours")
    exit()
else:
    pay = money_per_hour * 40 * overtime_multiplier
    pay += money_per_hour * (hours_worked - 40)

print("You earned ${}".format(pay))

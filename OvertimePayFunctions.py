# # calculate overtime pay - with FUNCTIONS!


# normal pay (no overtime)
def calcNormalPay(hours_worked, money_per_hour):
    return money_per_hour * hours_worked


# overtime pay
def calcOvertimePay(hours_worked, money_per_hour):
    pay = money_per_hour * 40 * 1.5
    pay += money_per_hour * (hours_worked - 40)
    return pay


# decide if overtime or not, and then print pay (before and after 20% income tax)
def calcPay(money_per_hour, hours_worked):
    pay = None
    if hours_worked > 40:
        pay = calcNormalPay(hours_worked, money_per_hour)
    else:
        pay = calcOvertimePay(hours_worked, money_per_hour)

    # format(float, ".2f") padds at least 2 decimals (eg. 1.3 to 1.30, and 2 to 2.00)
    print("Pay without tax is $" + format(pay, ".2f"))
    pay -= (pay * 0.20)
    print("Pay with tax is $" + format(pay, ".2f"))


# works at target
employee1_money_per_hour = 10
employee1_hours_worked = 40
print("\nEmployee 1: ${}/hour for {} hours".format(employee1_money_per_hour, employee1_hours_worked))
# should be $600 / $480.00
calcPay(employee1_money_per_hour, employee1_hours_worked)

# works at mcdonalds
employee2_money_per_hour = 8.75
employee2_hours_worked = 20
print("\nEmployee 2: ${}/hour for {} hours".format(employee2_money_per_hour, employee2_hours_worked))
# should be $350 / $280
calcPay(employee2_money_per_hour, employee2_hours_worked)

employee3_money_per_hour = 10
employee3_hours_worked = 10
print("\nEmployee 3: ${}/hour for {} hours".format(employee3_money_per_hour, employee3_hours_worked))
# should be $300 / $240
calcPay(employee3_money_per_hour, employee3_hours_worked)

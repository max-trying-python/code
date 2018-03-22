# static prices
priceOfDozenDonuts = 4.99
pricePerDonut = priceOfDozenDonuts / 12
cappucino = 2.99


def roundAndStr(num):
    return str(round(num, 2))


print("Change owed for first situation: " + roundAndStr(1 - pricePerDonut))
input("Press enter to continue...")

newPrice = round(20 - (2 * pricePerDonut) - cappucino, 2)
print("Change owed for second situation: " + roundAndStr(newPrice))
input("Press enter to exit...")

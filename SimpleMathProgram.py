priceOfDozenDonuts = 4.99
pricePerDonut = priceOfDozenDonuts / 12
cappucino = 2.99

print("Change owed for first situation: " + str(round(1 - pricePerDonut, 2)))
input("Press enter to continue...")

newPrice = round(20 - (2 * pricePerDonut) - cappucino, 2)
print("Change owed for second situation: " + str(newPrice))
input("Press enter to exit...")

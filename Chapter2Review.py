# chapter 2 review assignment


# book price
cover_price = 24.95
discount = 0.4
discounted_price = cover_price - (cover_price * discount)
price_for_60 = discounted_price + 3 + (discounted_price + 0.75) * 59
print("60 books: " + str(round(price_for_60, 2)))

# calculate seconds
leave_time = ((6 * 60) + 52) * 60
leave_time += 8 * 60 + 15
leave_time += (7 * 60 + 12) * 3
leave_time += 8 * 60 + 15

# calculate it in hours / minutes / seconds
seconds = round(leave_time % 60)
minutes = round((leave_time - seconds) / 60 % 60)
hours = round(((leave_time) / 60 - minutes) / 60)
seconds = str(seconds).zfill(1)
# .format is great
str_to_return = "You will arrive at {}:{}:{}".format(hours, minutes, seconds)
print(str_to_return)

# Convert grades in the evil 1-4 system to the great A-NC system

# the cancer that is the 1-4 system never ends
while True:
    try:
        # input the grade that the poor student who is under the torture that is the 1-4 system has recieved
        grade = float(input("\nPlease enter a grade from 1.0 - 4.0\n> "))
        if grade > 4 or grade < 1:
            print("Invalid grade.")
            continue
    # catch errors and tell the user they are bad.
    except Exception as e:
        print("Invalid grade.")
        # no student is an exception to the 1-4 system
        continue
    # if we're lucky, everything went well
    else:
        if grade >= 3.4:
            # you have to do more than is expected to get a grade that should be for anyone can do what they're asked
            print("Your grade is an A!")
        elif grade >= 2.8:
            # the grade that everyone is supposed to settle for is a B. you have to be content with this good but not great grade. good is the enemy of great.
            print("Your grade is a B.")
        elif grade >= 2.2:
            # you try very hard to go above and beyond. but becuase of a subjective rubric, your giant essay was not what the teacher wanted. therefore, it is below expectations, because the expectation is to please the teacher. therefore you get a 2 ish, which is a C. :feelsbadman:
            print("Your grade is a C :feelsbadman:")
        else:
            # you tried, but didn't do much. if your teacher is competent enough, than you get a 1 if you don't do the assignment. but a lot of teachers will add a "0" to the 1-4 system, meaning if you don't do the assignment, then you get a 0. if you did the assignment but did it bad enough, then you get a 1. this is unfair for each other grade, as it makes it harder to get higher grades in a system that already makes it harder.
            print("Your grade is a NC. Rip you.")

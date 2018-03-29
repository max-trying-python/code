while True:
    try:
        grade = float(input("Please enter a grade from 1.0 - 4.0\n"))
        if input > 4 or input < 1:
            continue
    except Exception as e:
        continue
    else:
        if grade >= 3.4:
            print("Your grade is an A!")
        elif grade >= 2.8:
            print("Your grade is a B.")
        elif grade >= 2.2:
            print("Your grade is a C :feelsbadman:")
        else:
            print("Your grade is a NC. Rip yous.")

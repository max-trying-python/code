# hardcoded numbers from assignment
numbers = [611, 612, 613, 617, 73, 77, 79, 5403, 5402, 5407, 669, 1188, 1189]


def isPrime(num):
    # basic input validation
    if type(num) != int:
        raise TypeError(str(num) + " was not a valid integer.")

    if num < 0:
        raise TypeError(str(num) + " was too low.")

    # if the number is less than 4, it is prime
    if num < 4:
        return True

    # the lambda that nobody understands.
    # if every number from 2 to the input does not produce an even number when the input
    # is divided by it, return True (it's a prime)
    # otherwise, return False (not a prime)
    return all(num % i != 0 for i in range(2, num))


formatted = "\n".join([str(num) + "\t" + str(isPrime(num)) for num in numbers])

print(formatted)

# A function that checks to see if a number is a prime number 
import math


def print_prime(in_number):
    # Declare variables and factor array
    loop = 1

    while loop <= int(in_number):
        # Loop through and divide by every possible number below "number" and store all factors appropriately
        quotient = math.modf(int(in_number) / loop)
        if quotient[0] == 0.0:
            if int(quotient[1]) == in_number:
                loop += 1
            elif int(quotient[1]) == 1:
                return in_number
            else:
                return ""
        else:
            loop += 1

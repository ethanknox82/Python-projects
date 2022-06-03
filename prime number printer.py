# This is a function that prints all the prime numbers leading up to the input number
import isprime


def prime_numbers(limit):
    # Declare variables
    i = 1
    j = 0
    nprime = []
    # loop through numbers
    while i <= int(limit):
        if isprime.print_prime(i):
            nprime.append(i)
            i += 1
            j += 1
        else:
            i += 1
    return print(f"prime numbers: {nprime}")


prime_numbers(input("Prime numbers leading up to: "))

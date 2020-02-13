# Q: What is the 10001st prime number?

import os

def is_prime_inefficient(i):
    # Loop through all the numbers from 2 to i-1, if the number is prime the mod won't be zero
    for j in range(2, i-1):
        if i % j == 0:
            return False
    return True

def is_prime_efficient(i):
    # https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    # todo
    return False

def main():
    prime_count_target = 10001
    prime_count = 0
    i = 2
    # Loop through natural numbers and find prime numbers
    while True:
        if is_prime_inefficient(i):
            prime_count = prime_count + 1
            if prime_count == prime_count_target:
                print(f'{ i } is the { prime_count_target }th prime number')
                break
        i = i + 1


if __name__ == '__main__':
    main()
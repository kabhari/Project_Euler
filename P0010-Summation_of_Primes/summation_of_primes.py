'''
Q: The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
'''

'''
final answer: 142913828922
'''

import numpy as np

# init constants
upper_bound = 2000000


def list_of_primes(n):
    # https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#Pseudocode
    numbers = [True for i in range(n)]
    numbers[0] = numbers[1] = False

    for p in range(1, int(n ** 0.5) + 1):
        if (numbers[p] == True):
            for i in range(p ** 2, n, p):
                numbers[i] = False

    primes = []
    for p in range(len(numbers)):
        if numbers[p]:
            primes.append(p)

    return np.array(primes,
                    dtype=object)  # sum is too large so need to set as object (https://stackoverflow.com/a/22664510)


if __name__ == '__main__':
    print("The sum of all the primes below two million is " + str(list_of_primes(upper_bound).sum()))

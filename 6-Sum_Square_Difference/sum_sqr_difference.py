# Q: Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

import time

def main():

    # Solution number 1
    sum_val = sum_of_sqr = 0
    upper_limit = 100
    for i in range(upper_limit + 1):
        sum_val += i
        sum_of_sqr += i**2

    # Print result
    print(sum_val**2 - sum_of_sqr)

    # Solution number 2
    sum_val = sum(i for i in range(1, upper_limit + 1))
    sum_of_sqr = sum(i**2 for i in range(1, upper_limit + 1))

    # Print result
    print(sum_val**2 - sum_of_sqr)


if __name__ == '__main__':
    main()
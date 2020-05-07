'''
Q: n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''


'''
final answer: 648
'''


# init constant
num = 100


# factorial
def factorial(n):
    m = n - 1
    if m >= 1:
        return n * factorial(m)
    else:
        return n


# compute
def compute():
    return sum([int(s) for s in str(factorial(num))])


if __name__ == '__main__':
    print("The sum of the digits in the number " + str(num) + "! is " + str(compute()))

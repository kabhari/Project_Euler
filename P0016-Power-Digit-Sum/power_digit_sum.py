'''
Q: 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2^1000?
'''

'''
final answer: 1366
'''

# init constant
pwr = 1000
base = 2


# compute
def compute():
    result = str(base ** pwr)
    digits = [int(d) for d in result]
    return (sum(digits))


if __name__ == '__main__':
    print("the sum of the digits of the number 2^1000 is " + str(compute()))

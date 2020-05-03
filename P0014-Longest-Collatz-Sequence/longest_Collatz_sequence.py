'''
Q:The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

'''
final answer: 837799
'''

# init constants
num = 1000000


def compute():
    # init
    max_counter = -1
    largest_chain = 0
    # loop through all the numbers to find the largest chain
    for i in range(num):
        n = i
        counter = 0
        while n > 1:
            if n % 2 == 0:  # even
                n = n // 2
            else:  # odd
                n = 3 * n + 1
            counter += 1
        # compare with max chain
        if counter > max_counter:
            largest_chain = i
            max_counter = counter
    # return result
    return largest_chain


if __name__ == '__main__':
    print("largest chain is produced by " + str(compute()))

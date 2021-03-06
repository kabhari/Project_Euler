'''
Q: The sequence of triangle numbers is generated by adding the natural numbers.
So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
'''

'''
final answer: 
'''

# init const numbers
div_num = 500


# method to compute nth triangle number
def compute_triangle(n):
    sum = 0
    for i in range(n + 1):
        sum += i
    return sum


def compute():
    # loop until answer is found
    n = 2  # we start from number 2 and up
    while True:
        tri = compute_triangle(n)
        # every number is divisible by 1 and itself so no point in going over them (other than 1 but we can safely ignore)
        counter = 2
        for i in range(2, tri):
            if tri % i == 0:
                counter = counter + 1
                if counter >= div_num:
                    return n
        n = n + 1


if __name__ == '__main__':
    print(compute())

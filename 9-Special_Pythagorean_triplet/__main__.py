# Q: A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = c^2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000, Find the product abc.


def main():
    print (find_abc(1000))

# We do this in a function to avoid breaking from nested loops and instead just return
def find_abc(total):
    # since a, b, c are natural numbers and a+b+c = 1000, they all cannot be larger than 998 or less than 1
    for a in range(1, total - 2): # -2 bc the minimum value for b and c is 1 (natural numbers)
        for b in range(a + 1, total - 2):
            c = total - a - b
            if a * a + b * b == c * c:
                return (a*b*c) # the question specifies there exists exactly one case so we can return at this point

if __name__ == '__main__':
    main()

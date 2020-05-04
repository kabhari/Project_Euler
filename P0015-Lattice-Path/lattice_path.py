'''
Q: Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly
6 routes to the bottom right corner. How many such routes are there through a 20×20 grid?
'''

'''
final answer: 137846528820
'''

grid_size = 20


def factorial(n):
    m = n - 1
    if m >= 1:
        return n * factorial(m)
    else:
        return n


def compute():
    # in a X by X grid, we have (X * 2)! possible permutations - however, since we only have two possible moves (right and
    # down), then we have X! * 2 movements (X! for down and X! for right) that make no difference, so overall we have
    # X^2! / ( X! * X!) possible routes
    return factorial(grid_size * 2) / (factorial(grid_size) ** 2)


if __name__ == '__main__':
    print("There are " + str(int(compute())) + " routes through a 20 by 20 grid")

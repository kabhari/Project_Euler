'''
Q:If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115
(one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
'''

'''
final answer: 21124
'''

# init constant
num_1_9 = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
num_11_19 = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
num_10s = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
num_100s = ["hundred"]
num_1000s = "one thousand"
extra = "and"


def compute():
    sum = 0
    for i in range(1, 1001):  # 1000 is inclusive
        if i >= 1 and i < 10:  # 1 to 9
            sum += len(num_1_9[i])
        elif i >= 11 and i < 20:  # 11 to 19
            sum += len(num_11_19[i % 10])
        elif i >= 10 and i < 100:  # 20 to 99 + 10
            sum += len(num_10s[i // 10]) + len(num_1_9[i % 10])
        elif i >= 100 and i < 1000:  # 100 to 999
            if i % 100 != 0:  # add 'and' to all numbers between 100 and 1000 but 100, 200, 300, ...
                sum += len(extra)
            if i % 100 >= 11 and i % 100 < 20:  # 111, 112, 123,.., 211, 212, ..., 919 are special cases
                sum += len(num_1_9[i // 100]) + len(num_11_19[i % 10]) + len(num_100s[0])
            else:  # the rest...
                sum += len(num_1_9[i // 100]) + len(num_10s[(i // 10) % 10]) + len(num_1_9[i % 10]) + len(num_100s[0])
        else:  # and finally 1000
            sum += len(num_1000s) - num_1000s.count(' ')

    return sum


if __name__ == '__main__':
    print("there are " + str(compute()))

'''
Q:You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''

'''
final answer: 171
'''


# init constant
months = [
    31, # Jan
    -1, # Feb - this will be filled later depending on the year
    31, # Mar
    30, # Apr
    31, # May
    30, # Jun
    31, # Jul
    31, # Aug
    30, # Sep
    31, # Oct
    30, # Nov
    31, # Dec
]

def compute_sundays(start, end):
    sun_sum = 0
    remainder = 0

    for y in range(start, end + 1):
        months[1] = 28 + (y % 4 == 0 and y % 400 == 0);
        for m in range(len(months)):
            remainder += months[m] % 7
            if remainder >= 7:
                remainder = remainder % 7
            if remainder == 6:
                sun_sum += 1
    return sun_sum

# compute
def compute():
    return compute_sundays(1901, 2000)

if __name__ == '__main__':
    print(" " + str(compute()) + " ")

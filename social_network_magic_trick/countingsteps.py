import math

def time(n):
    """ Return the number of steps 
    necessary to calculate
    `print countdown(n)`"""
    steps = 0
    # YOUR CODE HERE
    # check for while condition, run two things in while loop = 3
    # declare y, print y = 2
    # x divided by 5 until 0, so we have n / 5
    steps += 3 + 2 * math.ceil(n / 5.0) # in one iteration, it has 5 steps
    return steps

def countdown(x):
    y = 0
    while x > 0:
        x = x - 5
        y = y + 1
    print(y)

print(countdown(50))
# print(time(50))

# print(countdown(15))
# print(countdown(1))
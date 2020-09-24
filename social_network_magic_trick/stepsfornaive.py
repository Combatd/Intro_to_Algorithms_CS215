# counting steps in naive as a function of a

def naive(a, b):
    x = a
    y = b
    z = 0
    while x > 0:
        z = z + y
        x = x - 1
    return z

'''
    until x (based on value of a) gets to 0, it runs 2 things in loop.
    2a
    we have to assign the values of 3 variables
    3
'''

def time(a):
    # The number of steps it takes to execute naive(a, b)
    # as a function of a
    steps = 0
    # your code here
    steps = 2 * a + 3
    return steps
def russian(a,b):
    x = a; y = b
    z = 0
    while x > 0:
        if x % 2 == 1: z = z + y
        y = y << 1
        x = x >> 1
    return z

# Test Data
print(russian(10,10))
print(russian(11,14))
print(russian(20,7))

''' 
Algorithm Analysis 
We should be able to find out how many additions in russian(20,7).
a = 20 and b = 7.
We set x = a and y = b, so x = 20 and y = 7.
z = 0 as an accumulator
If x / 2 has a remainder of 1, then we add 7 to our accumulator z

Trying to step through the algorithm...
We move the binary digits (base 2) to add the value TWICE when y is added into z.
It happens at 5 and 1!
'''
def naive(a, b):
    x = a
    y = b
    z = 0
    while x > 0:
        z = z + y
        x = x - 1
    return z

# Test Data
print(naive(1, 2)) # 1 * 2 = 2
print(naive(5, 10)) # 5 * 10 = 50
print(naive(25, 75)) # 25 * 75 = 1875

'''
    This naive function is actually a mathematical proof that a product
    of two numbers multiplied together is actually the sum of one number
    being added to itself by the second number's value times.
'''
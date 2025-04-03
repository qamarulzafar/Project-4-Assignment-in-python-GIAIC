# Implement the following function which takes in 3 integers as parameters:

# def in_range(n, low, high) """ Returns True if n is between low and high, inclusive. high is guaranteed to be greater than low. """



def in_range(n, low, high):
    if low <= n <= high:
        return True
    else:
        return False
    

print(in_range(5, 1, 10))   # True (5 is in range)
print(in_range(1, 1, 10))   # True (1 is inclusive)
print(in_range(10, 1, 10))  # True (10 is inclusive)
print(in_range(15, 1, 10))  # False (15 is outside the range)
print(in_range(0, 1, 10))   # False (0 is outside the range)

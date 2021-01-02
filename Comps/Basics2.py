import random
import math

# Create the array
N = 30
RANGE = 200
a = [random.randint(0, RANGE) for i in range(N)]
print(a)

# Create a new array b that has just the even numbers in a
def just_evens(x):
    evens = []
    for element in x:
        if element % 2 == 0:
            evens.append(element)

    return evens

b = just_evens(a)
print(b)


# Create a new array c that has just the perfect squares in a
# That is, numbers such as 1, 4, 9, 16, 25, ...
def just_squares(x):
    squares = []
    for element in x:
        if math.sqrt(element) % 1 == 0:
            squares.append(element)
    return squares

c = just_squares(a)
print(c)


# Let's create another array, capital A
A = [random.randint(0, RANGE/2) for i in range(N)]
print(A)

# Print all the elments of a that are greater than the
# largest element of A


# Builds a list of all elements of x that are larger than
# every element of X
def larger_than_largest(x, X):
    larger_x = []
    for element in x:
        if element > max(X):
            larger_x.append(element)
    return larger_x

d = larger_than_largest(a, A)
print("The list of numbers larger than the largest is " + str(d))

# Returns True if and only if n is prime: 2, 3, 5, 7, 11, 13, ...
def is_prime(n):
    if n <= 0:
        return False
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False

    return True


# Print just the prime numbers in a
for element in a:
    if is_prime(element):
        print(element)

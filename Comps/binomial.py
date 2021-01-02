# Finds binomial coefficients using the recurrence:
# b(n, k) = b(n-1, k) + b(n-1, k-1)


def b(n, k):
    if n == 0 or n == k:
        return 1

    return b(n-1, k) + b(n-1, k-1)


# Now print some values for testing
print(b(6, 2))
print(b(10, 5))
print(b(12, 1))
print(b(20, 10))
print(b(25, 12))
print(b(100, 100))

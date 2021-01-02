# Computes the g function on pairs of non-negative integers
memo = {}

def g(a, b):
    #global memo
    if a == 0: return b
    if b == 0: return a+1
    if (a, b) in memo:
        return memo[(a, b)]

    sum = 0
    for i in range(a):
        sum += g(i, b-1)

    memo[(a, b)] = sum


    return sum



# Now print some values for testing
print(g(6, 2))
print(g(10, 5))
print(g(12, 1))
print(g(20, 10))
print(g(25, 12))
print(g(100, 100))
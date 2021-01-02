import sys
for i in sys.stdin:
    x = int(i)


    def factorial(n):
        if n == 1:
            return 1
        else:
            return n * factorial(n - 1)

    print(factorial(x))




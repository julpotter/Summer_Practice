n1 = 0
n2 = 1

for i in range(1000):
    new = n1 + n2
    n1 = n2
    n2 = new
    print(n1)


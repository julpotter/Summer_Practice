testlist = [1, 4, 6, 4, 2, 4, 9]
memo = []
for element in testlist:
    if element in memo:
        print("There is duplicate entry " + str(element) + "!")
        break
    memo.append(element)
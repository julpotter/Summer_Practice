from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        first = True
        N = len(digits)

        for i in range(N - 1, -1, -1):

            if first:
                digits[i] += 1
                first = False
            if carry == 1:
                digits[i] += 1
                carry = 0
            if digits[i] > 9:
                digits[i] = 0
                carry = 1

            # print(i)
            # print(digits[i])

        if carry == 1:
            digits.insert(0, 1)
            digits[1] = 0

        return digits


Input = [8, 9, 9, 9]
print(Solution.plusOne(Solution, Input))
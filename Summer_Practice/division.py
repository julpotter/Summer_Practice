class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        add = 0
        quotient = 0
        positive = True
        while add + abs(divisor) <= abs(dividend):
            add += abs(divisor)
            quotient += 1

        if dividend < 0 and divisor < 0:
            positive = True
        elif dividend > 0 and divisor > 0:
            positive = True
        else:
            positive = False

        if not positive:
            quotient = ~quotient + 1

        return quotient


assert (Solution.divide(Solution, -1, 1)) == -1





class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        left = set(["{", "[", "("])
        parentheses_dict = {"{": "}", "[": "]", "(": ")"}

        for element in s:
            if element in left:
                stack.append(element)
                print(stack)
                print(stack[-1])
                continue
            else:
                if parentheses_dict[element] == stack[-1]:
                    stack.pop()


check = "{[]}"
if Solution.isValid(Solution, check):
    print("True")
else:
    print("False")
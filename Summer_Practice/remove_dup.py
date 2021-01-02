from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        N = len(nums)
        for i in range(N - 1):
            # print(output[i])
            if nums[i] == nums[i + 1]:
                del nums[i]
            else:
                i += 1

        return nums

number_list = [1, 1, 2]
print(Solution.removeDuplicates(Solution, number_list))

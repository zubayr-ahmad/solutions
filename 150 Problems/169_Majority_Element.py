# https://leetcode.com/problems/majority-element/description/?envType=study-plan-v2&envId=top-interview-150
from collections import Counter
class Solution:
    def majorityElement(self, nums) -> int:
        dict = Counter(nums)
        max_val = 0
        max_num = float("-inf")
        for i,j in dict.items():
            if j > max_val:
                max_val = j
                max_num = i
        return max_num




sol = Solution()
nums = [3,2,3]
# nums = [2,2,1,1,1,2,2]
# nums = [6,5,5]
print(sol.majorityElement(nums))
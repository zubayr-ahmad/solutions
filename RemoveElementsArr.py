# https://leetcode.com/problems/remove-element/?envType=problem-list-v2&envId=array
class Solution:
    def removeElement(self, nums, val: int) -> int:
        i = 0
        count = 0
        replace = len(nums) - 1
        while i < len(nums) and replace >= i and nums[replace] != -1:
            if nums[i] == val:
                nums[i] = -1
                nums[i], nums[replace] = nums[replace], nums[i]
                replace -= 1
                continue
            count += 1
            i = i + 1
        nums = nums[:count]
        return count, nums

sol = Solution()
# nums = [3,2,2,3]
nums = [0,1,2,2,3,0,4,2]
val = 2
print(sol.removeElement(nums, val))
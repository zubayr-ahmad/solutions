# https://leetcode.com/problems/rotate-array/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if len(nums) == k:
            return 
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])
        
sol = Solution()
nums = [1,2,3,4,5,6,7]
k = 10
sol.rotate(nums, k)
print(nums)

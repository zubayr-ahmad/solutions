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
        stopage = len(nums) - k
        sliced = nums[stopage:]
        
        place = len(nums) - 1
        j = stopage - 1
        while j >= 0:
            nums[place] = nums[j]
            j -= 1
            place -= 1
        
        nums[:k] = sliced
        
sol = Solution()
nums = [1,2,3,4,5,6,7]
k = 10
sol.rotate(nums, k)
print(nums)

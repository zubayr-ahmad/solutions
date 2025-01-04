# https://leetcode.com/problems/rotate-array/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) == k:
            return 
        elif k < len(nums):
            stopage = len(nums) - k
            sliced = nums[stopage:]
            
            place = len(nums) - 1
            j = stopage - 1
            while j >= 0:
                nums[place] = nums[j]
                j -= 1
                place -= 1
            
            for i in range(len(sliced)):
                nums[i] = sliced[i]
                
            return 
        elif k > len(nums):
            remaining = k % len(nums)
            return self.rotate(nums, remaining)
        
sol = Solution()
nums = [1,2,3,4,5,6,7]
k = 10
sol.rotate(nums, k)
print(nums)

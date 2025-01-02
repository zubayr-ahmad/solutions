class Solution:
    def subarraySum(self, nums, k: int) -> int:
        subarrays = []
        count = 0
        for val in nums:    # iterating to get single values
            if val == k:
                count += 1
        
        for i in range(0,len(nums)):
            left = i
            right = left + 1
            for j in range(left, right):
                if nums[left:j+1] == k:
                    count += 1
        return count
                
sol = Solution()
nums = [1,1,1]
k = 2
print(sol.subarraySum(nums, k)) 
            
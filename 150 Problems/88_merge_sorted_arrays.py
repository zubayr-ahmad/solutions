# Link: https://leetcode.com/problems/merge-sorted-array
class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        place = 0
        for i in range(len(nums2)):
            for j in range(len(nums1)):
                if nums2[i] > nums1[place] and nums1[place] != 0:
                    place = place + 1
                    continue
                break
            nums1.insert(place,nums2[i])
            nums1.pop(-1)
        return nums1
    
sol = Solution()
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
print(sol.merge(nums1,m,nums2,n))
# Link: https://leetcode.com/problems/merge-sorted-array
class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):  # nums2
            for j in range(m):  # nums1
                if nums2[i]<= nums1[j]:
                    nums1.insert(j, nums2[i])
                    m = m + 1
                    nums1.pop()
                    break
            else:
                nums1.insert(m, nums2[i])
                m = m + 1
                nums1.pop()
        return nums1
    
sol = Solution()
nums1 = [-1,0,0,3,3,3,0,0,0]
m = 6
nums2 = [1,2,2]
n = 3
# nums1 = [1,2,3,0,0,0]
# nums2 = [2,5,6]
# m = 3
# n = 3
print(sol.merge(nums1,m,nums2,n))
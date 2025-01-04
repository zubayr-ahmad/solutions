class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev_num = nums[0]
        val_count = 1
        remove_count = 0
        i = 1
        while i < len(nums):
            if nums[i] == prev_num and val_count == 2:
                nums.pop(i)
                remove_count += 1
            elif prev_num == nums[i]:
                val_count += 1
                i += 1
            elif prev_num != nums[i]:
                prev_num = nums[i]
                val_count = 1
                i += 1
        return len(nums) - remove_count

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test 1: Array with duplicates more than twice
    nums1 = [1,1,1,2,2,3]
    length1 = solution.removeDuplicates(nums1)
    print(f"Test 1: Input array after removal: {nums1}, Length: {length1}")
    # Expected: [1,1,2,2,3], Length: 5
    
    # Test 2: Array with no duplicates
    nums2 = [1,2,3,4,5]
    length2 = solution.removeDuplicates(nums2)
    print(f"Test 2: Input array after removal: {nums2}, Length: {length2}")
    # Expected: [1,2,3,4,5], Length: 5
    
    # Test 3: Array with all same elements
    nums3 = [1,1,1,1,1]
    length3 = solution.removeDuplicates(nums3)
    print(f"Test 3: Input array after removal: {nums3}, Length: {length3}")
    # Expected: [1,1], Length: 2
    
    # Test 4: Array with multiple groups of duplicates
    nums4 = [1,1,1,2,2,2,3,3,3,4]
    length4 = solution.removeDuplicates(nums4)
    print(f"Test 4: Input array after removal: {nums4}, Length: {length4}")
    # Expected: [1,1,2,2,3,3,4], Length: 7
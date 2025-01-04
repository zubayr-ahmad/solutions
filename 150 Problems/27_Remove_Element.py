# https://leetcode.com/problems/remove-element/?envType=study-plan-v2&envId=top-interview-150

import unittest

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        replace_pointer = len(nums) - 1
        count = 0
        while i <= len(nums) and i <= replace_pointer:
            if nums[i] == val:
                nums[i], nums[replace_pointer] = nums[replace_pointer], nums[i]
                replace_pointer -= 1
                count += 1
                continue
            i += 1
        return len(nums) - count

class TestSolution(unittest.TestCase):
    def setUp(self):
        # This method runs before every test case
        self.solution = Solution()

    def test_case_1(self):
        nums = [3, 2, 2, 3]
        val = 3
        length = self.solution.removeElement(nums, val)
        self.assertEqual(length, 2)
        self.assertTrue(all(num != val for num in nums[:length]))

    def test_case_2(self):
        nums = [0, 1, 2, 2, 3, 0, 4, 2]
        val = 2
        length = self.solution.removeElement(nums, val)
        self.assertEqual(length, 5)
        self.assertTrue(all(num != val for num in nums[:length]))

    def test_case_3(self):
        nums = []
        val = 1
        length = self.solution.removeElement(nums, val)
        self.assertEqual(length, 0)
        self.assertTrue(all(num != val for num in nums[:length]))

    def test_case_4(self):
        nums = [1, 1, 1, 1]
        val = 1
        length = self.solution.removeElement(nums, val)
        self.assertEqual(length, 0)
        self.assertTrue(all(num != val for num in nums[:length]))

    def test_case_5(self):
        nums = [1, 2, 3, 4]
        val = 5
        length = self.solution.removeElement(nums, val)
        self.assertEqual(length, 4)
        self.assertTrue(all(num != val for num in nums[:length]))

# Run tests when this file is executed
if __name__ == '__main__':
    unittest.main()

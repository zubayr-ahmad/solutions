# https://leetcode.com/problems/valid-palindrome/
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new_str = self.correct_string(s)

        if len(new_str) == 1 or len(new_str) == 0:
            return True
        half_len = len(new_str) // 2
        for i in range(half_len + 1):
            if new_str[i] == new_str[len(new_str)-1 - i]:
                continue
            return False
        return True
    def correct_string(self, s):
        new_str = []
        for char in s:
            char = char.lower()
            if char.isalnum():
                new_str.append(char)
        return new_str

sol = Solution()
s = "A man, a plan, a canal: Panama"
s = "race a car"
s = ' '
print(sol.isPalindrome(s))
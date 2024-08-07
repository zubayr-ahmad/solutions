# https://leetcode.com/problems/valid-palindrome/
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        first = 0
        last = len(s) - 1
        while first <= last:
            fchar = s[first].lower()
            lchar = s[last].lower()
            if not fchar.isalnum():
                first += 1
            elif not lchar.isalnum():
                last -= 1
            else:
                if fchar != lchar:
                    return False
                first += 1
                last -= 1
        return True
            
            
sol = Solution()
s = "A man, a plan, a canal: Panama"
# s = "race a car"
# s = ' '
print(sol.isPalindrome(s))
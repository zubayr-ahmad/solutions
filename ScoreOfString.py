# https://leetcode.com/problems/score-of-a-string/
class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        for idx in range(len(s)-1):
            result += abs(ord(s[idx]) - ord(s[idx+1]))
        return results
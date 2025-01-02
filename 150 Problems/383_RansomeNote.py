# https://leetcode.com/problems/ransom-note/?envType=study-plan-v2&envId=top-interview-150
from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cr = Counter(ransomNote)
        cm = Counter(magazine)
        for key in ransomNote:
            r = cm.get(key)
            if r:
                cm[key] -= 1
                continue
            return False
        return True

sol = Solution()
ransomNote = "aa"
magazine = "ab"
print(sol.canConstruct(ransomNote,magazine))  
# https://leetcode.com/problems/isomorphic-strings/description/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict1 = {}
        for idx, char in enumerate(s):
            if char in dict1:
                if dict1[char] != t[idx]:
                    return False
            elif t[idx] in dict1.values():
                return False
            dict1[char] = t[idx]
        return True



sol = Solution()
s= "badc"
t = "baba"
print(sol.isIsomorphic(s,t))
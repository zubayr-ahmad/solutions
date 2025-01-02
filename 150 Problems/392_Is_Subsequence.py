#https://leetcode.com/problems/is-subsequence/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        pointer = 0
        flag = False
        for i, val in enumerate(t):
            if s[pointer] == val:
                pointer += 1
                if pointer == len(s):
                    flag = True
                    break
        return flag

            


sol = Solution()
s = "abc"
t = "ahbgdc"
print(sol.isSubsequence(s, t))
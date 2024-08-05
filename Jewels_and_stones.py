# https://leetcode.com/problems/jewels-and-stones/
class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        count = 0
        stones_list = list(stones)
        for i in stones_list:
            if i in jewels:
                count += 1
        return count
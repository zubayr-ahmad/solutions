class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        # dict1 = {}
        # for char in alphabets:
        #     dict1[ord(char) - 64] = char
        result = ''
        while columnNumber > 26:
            letter_idx = columnNumber % 26
            columnNumber = columnNumber // 26
            # if letter_idx == 0:
            result += alphabets[letter_idx - 1]
        if columnNumber:
            result += alphabets[columnNumber - 1]
        return result[::-1]

sol = Solution()
column = 52
print(sol.convertToTitle(column))
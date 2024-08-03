# https://leetcode.com/problems/latest-time-you-can-obtain-after-replacing-characters/
def findLatestTime(s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        s.remove(':')
        s = ''.join(s)
        values = [0,0,0,0]
        for idx, char in enumerate(s):
            if char == '?':
                values[idx] = -1
                continue
            values[idx] = int(char)
        
        for idx, num in enumerate(values):
            if num == -1:
                if idx == 0:
                    if values[1] > 1:
                        values[0] = 0
                    else:
                        values[0] = 1
                elif idx == 1:
                    if values[0] == 1:
                        values[1] = 1
                    else:
                        values[1] = 9
                elif idx == 2:
                    values[2] = 5
                elif idx == 3:
                    values[3] = 9

        return f"{values[0]}{values[1]}:{values[2]}{values[3]}"

if __name__ == "__main__":
    s = "1?:?4"
    print(findLatestTime(s)) # 19:54
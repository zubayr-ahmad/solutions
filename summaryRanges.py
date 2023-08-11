class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        rangeList = []
        i = 0
        if len(nums) == 0:
            return rangeList
        elif len(nums) == 1:
            rangeList.append(str(nums[0]))
            return rangeList
        elif len(nums) == 2:
            if (nums[1] == nums[0]):
                rangeList.append(str(nums[0]))   
            elif (nums[1]-nums[0]) == 1:
                rangeList.append(str(nums[0])+'->'+str(nums[1]))
            else:
                rangeList.append(str(nums[0]))
                rangeList.append(str(nums[1]))
            return rangeList
        start = nums[0]
        end = nums[0]
        while i <len(nums)-1:
            var1 = nums[i]
            var2 = nums[i+1]
            sub = abs(var1-var2)
            if 0 < (sub) <= 1:
                end = nums[i+1]
            else:
                tup = [start,end]
                rangeList.append(tup)
                start = nums[i+1]
                end = nums[i+1]
            i += 1
        if 0 < abs(nums[-2]-nums[-1])<=1:
            rangeList.append([start,end])
        else:
            rangeList.append((nums[-1],nums[-1]))
        output = self.stringOutput(rangeList)
        return output
    def stringOutput(self,list):
        outputList = []
        for i in list:
            if i[0]==i[1]:
                outputList.append(str(i[0]))
            else:
                st=str(i[0]) + '->'+ str(i[1])
                outputList.append(st)
        return outputList


if __name__ == '__main__':
    p = Solution()
    nums = [0,1,2,4,5,7]
    nums1 = [0,2,3,4,6,8,9]

    p.summaryRanges(nums1)
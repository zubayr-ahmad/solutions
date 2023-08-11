class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        solutionList = []
        if len(nums) >1:
            for i,vali in enumerate(nums):
                for j,valj in enumerate(nums):
                    if i != j:
                        if vali + valj == target:
                            solutionList.append(i)
                            solutionList.append(j)
                            return solutionList
        return nums        


    # Better approach
    def twoSum02(self, nums: list[int], target: int) -> list[int]:
        num_dict = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[num] = i
        return []  # No solution found


if __name__ == '__main__':
    p = Solution()
    nums = [0,1,2,4,5,7]
    nums1 = [0,2,3,4,6,8,9]

    print(p.twoSum(nums1,8))
# https://leetcode.com/problems/search-insert-position/

def searchInsert(nums, target):
    if target <= nums[0]:
        return 0
    for i in range(1,len(nums)):
        if target <= nums[i]:
            return i
    return len(nums)

if __name__ == '__main__':
    nums = [1,3,5,6]
    target = 5
    print(searchInsert(nums,target))
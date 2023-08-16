# https://leetcode.com/problems/sliding-window-maximum/

def maxSlidingWindow(nums, k):
    resultArr = []
    window = nums[:k]  # slicing arr to get window
    maxNum = max(window)
    indexofMax = nums.index(maxNum)
    resultArr.append(maxNum)
    for i in range(k,len(nums)):
        indexDifference = abs(indexofMax - i)
        if nums[i] < maxNum and indexDifference < k:
            resultArr.append(maxNum)
            continue
        window = nums[i-k+1:i+1]
        maxNum = max(window)
        indexofMax = nums.index(maxNum)
        resultArr.append(maxNum)
    return resultArr


if __name__ == '__main__':
    # nums = [1,3,-1,-3,5,3,6,7]
    nums = [1,-1]
    k = 1
    print(maxSlidingWindow(nums,k))

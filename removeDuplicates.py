def removeDuplicates(nums):
    prev = nums[0]
    new = [prev]
    for i in range(1, len(nums)):
        if nums[i] == prev:
            continue
        new.append(nums[i])
        prev = nums[i]
    return len(new),new

if __name__ == '__main__':
    arr = [0,0,1,1,1,2,2,3,3,4]
    arr2 = [-22,2,5,6,7,7,8,9,120,122,122,123,123,1000,10002]
    print(removeDuplicates(arr2))
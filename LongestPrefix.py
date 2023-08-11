def longestPrefix(strs):
    # Finding the minimum length to run the loop upto it
    # arrOfLengths = []
    # for i in strs:
    #     arrOfLengths.append(len(i))
    # minimum = min(arrOfLengths)
    #
    # # storing the minimum string for comparing
    # for i in strs:
    #     if minimum == len(i):
    #         minString = i
    minString = min(strs, key=len)
    minimum  = len(minString)
    result = ''
    flag = True     # Flag to find first mismatch
    for i in range(minimum):    # Run loop upto minimum length
        for j in strs:
            if (j[i] != minString[i]):  # If there is mismatch with the minString
                flag = False
        if flag == False:
            break
        result += j[i]  # If char is present in all the strings then flag remains True and we add it in the result
    return result
    
if __name__ == '__main__':
    arr = ['folowfloightfolow','folowfloightfolowflower','folowfloight']
    print(longestPrefix(arr))
    # arr2 = [2,3,4,6,7,8,9]
    # print(min(arr2))
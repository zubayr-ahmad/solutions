# https://leetcode.com/problems/plus-one/
def plusOne(digits):
    carry = 1
    arr = []
    for i in reversed(digits):
        if carry != 0:
            i = i + carry
            if i > 9:
                carry = int(str(i)[0])
                i = i % 10
            else:
                carry = 0
        arr.append(i)
    if carry != 0:
        arr.append(carry)
    return arr[::-1]

if __name__ == '__main__':
    # arr = [1,2,4,9,9,9]
    arr = [9]
    print(plusOne(arr))
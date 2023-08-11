from copy import copy

def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    list = []
    new = x
    while x >= 10 :
        rem = x%10
        x = x//10
        list.append(rem)
    list.append(x)
    list.reverse()
    y = list[-1]
    for i in range(1,len(list)):
        y = y + list[i]*(10**i)
    return y == new

# Short code
def isPalindrome02(x: int) -> bool:
    if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
    reversed_num = 0
    original_num = x
    
    while x > 0:
        # Build the reversed number by extracting the last digit from x
        reversed_num = reversed_num * 10 + x % 10
        # Reduce x by removing the last digit
        x //= 10
    
    # At this point, the original number is reversed
    # If they are equal, the original number is a palindrome
    return original_num == reversed_num


if __name__=='__main__':
    num = 10
    print(isPalindrome(num))
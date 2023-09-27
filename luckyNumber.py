def findLucky(num):
    if num % 4 == 0 or num % 7 == 0:
        return "YES"
    for i in range(2,num):
        if num % i == 0:
            if find(i) == "YES":
                return "YES"

    num = str(num)
    return find(num)
    
def find(num):
    char = '47'
    for i in str(num):
        if i not in char:
            return "NO"
    return "YES"

num = int(input())
print(findLucky(num))
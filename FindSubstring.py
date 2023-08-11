def strStr(haystack, needle):
    for i, char in enumerate(haystack):
        if char == needle[0]:
            status=find(haystack,needle,i)
            if status: return i
            continue
    return -1



def find(haystack, needle, index):
    try:
        if haystack[index:index + len(needle)] == needle:
            return True
        return False
    except:
        return False

# Much better Method
def findSubStr(haystack, needle):
    if len(needle) == 0:
        return 0
    elif needle not in haystack:
        return -1
    return haystack.index(needle)

if __name__ == '__main__':
    haystack = "sadbutsad"
    needle = "sadbr"
    print(strStr(haystack,needle))
    print(findSubStr(haystack,needle))
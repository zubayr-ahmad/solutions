
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        tmp = l1
        sum1 = 0
        while tmp.next != None:
            sum1 += tmp.val
            tmp = tmp.next
        sum1 += tmp.val
        tmp = l2
        sum2 = 0
        while tmp.next != None:
            sum2 += tmp.val
            tmp = tmp.next
        sum2 += tmp.val
        print(sum1,sum2)

if __name__ == '__main__':
    l1 = ListNode(1,3)
    l1.next = 3
        

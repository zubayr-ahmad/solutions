class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def createList(arr, startingNode):
    tmp = startingNode
    for i in arr:
        node = ListNode(i)
        tmp.next = node
        tmp = tmp.next


def displayList(list):
    c = list
    while c.next != None:
        print(c.val, end=' ')
        c = c.next
    print(c.val)

def insertLast(list1,val):
    for index, element in reversed(list(enumerate(list1))):
        if val >= element:
            list1.insert(index + 1, val)
            break
    else:
        list1.insert(0, val)





class Solution:
    def mergeTwoLists(self, list1, list2):
        if list1 == None:
            if list2 == None:
                return ListNode('')
            return list2
        elif list2 == None:
            return list1
        currentOfList1 = list1
        currentOfList2 = list2
        list3 = []
        tmp1 = currentOfList1
        tmp2 = currentOfList2
        while currentOfList1.next != None and currentOfList2.next != None:
            if currentOfList1.val <= currentOfList2.val:
                list3.append(currentOfList1.val)
                currentOfList1 = currentOfList1.next
                continue
            elif currentOfList2.val <= currentOfList1.val:
                list3.append(currentOfList2.val)
                currentOfList2 = currentOfList2.next
                continue

        if currentOfList1.next == None:
            tmp = currentOfList2
            while tmp.next != None:
                list3.append(tmp.val)
                tmp = tmp.next
            list3.append(tmp.val)
            insertLast(list3, currentOfList1.val)

        elif currentOfList2.next == None:
            tmp = currentOfList1
            while tmp.next != None:
                list3.append(tmp.val)
                tmp = tmp.next
            list3.append(tmp.val)
            insertLast(list3, currentOfList2.val)
        list4 = ListNode(list3[0])
        createList(list3[1:], list4)
        return list4










if __name__ == "__main__":
    l1 = ListNode(-9)
    l = [3]
    createList(l, l1)

    l2 = ListNode(5)
    l_2 = [7]
    createList(l_2, l2)
    s = Solution()
    displayList(s.mergeTwoLists(l1,l2))

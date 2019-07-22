# Definition for singly-linked list.
class ListNode(object):
    val = 0
    next = None
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(l1.val + l2.val)
        pl1 = l1.next
        pl2 = l2.next
        pt = result
        while pl1 != None or pl2 != None:
            if pl1 != None:
                if pl2 != None:
                    pr = ListNode(pl1.val + pl2.val)
                    pl2 = pl2.next
                else:
                    pr = ListNode(pl1.val)
                pl1 = pl1.next
            else:
                pr = ListNode(pl2.val)
                pl2 = pl2.next
            pt.next = pr
            pt = pt.next
        pt = result
        while True:
            if pt.val > 9:
                if pt.next == None:
                    pt.next = ListNode(0)
                pt.val -=10
                pt.next.val += 1
            if pt.next == None:
                break
            pt = pt.next
        return result


if __name__ == '__main__':
    num1 = '0'
    num2 = '0'
    l1 = ListNode(int(num1[len(num1) - 1]))
    l2 = ListNode(int(num2[len(num2) - 1]))
    pl1 = l1
    pl2 = l2
    for i in range(len(num1) - 2, -1, -1):
        pl1.next = ListNode(int(num1[i]))
        pl1 = pl1.next
    for i in range(len(num2) - 2, -1, -1):
        pl2.next = ListNode(int(num2[i]))
        pl2 = pl2.next

    s = Solution()
    result = s.addTwoNumbers(l1, l2)
    while True:
        print(result.val)
        result = result.next
        if result == None:
            break



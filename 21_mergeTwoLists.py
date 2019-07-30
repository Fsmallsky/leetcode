# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and  not l2: return None
        head = ListNode(0)
        tail = head
        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                tail, l1 = tail.next, l1.next
            else:
                tail.next = l2
                tail, l2 = tail.next, l2.next
        if l1: tail.next = l1
        if l2: tail.next = l2
        return head.next
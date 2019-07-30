# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        pnode = head
        tail = head
        for x in range(n):
            pnode = pnode.next
        if pnode == None:
            return head.next
        while pnode.next:
            pnode = pnode.next
            tail = tail.next
        tail.next = None
        return head

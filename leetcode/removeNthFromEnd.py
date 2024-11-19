# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        2 pointers, curr and n
        curr starts from head
        n starts from nth node from head
        when curr = curr.next, n = n.next
        when n is none. curr is on nth node from the back.
        remove this node.
        to do that, link prev.next = curr.next
        """
        prev = None
        curr = head
        nth = head

        if head.next == None:
            if n == 1:
                return None
            else:
                return head

        while n > 0:
            nth = nth.next
            n -= 1

        while nth != None:
            prev = curr
            curr = curr.next
            nth = nth.next

        if prev:
            prev.next = curr.next
        else:
            head = head.next
            
        return head
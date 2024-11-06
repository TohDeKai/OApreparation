# https://leetcode.com/problems/reverse-linked-list-ii/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """
        traverse through the node until you reach the leftNode
        then you begin reversing
        when you traverse you keep track of curr and prev

        to swap
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

        leftInList
        leftOutOfList

        rightInList
        rightOutOfList

        keep track of these 4 ^

        when you finish the swaps
        connect leftOutOfList next to rightInList
        connect rightOutOfList next to leftInList
        """

        if left == right:
            return head

        count = 1
        curr = head
        prev = None

        leftInList = None
        leftOutOfList = None
        
        while curr and count <= right:
            print(curr)
            if count < left:
                prev = curr
                curr = curr.next
                
            elif count == left:
                leftOutOfList = prev
                leftInList = curr

                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            elif count > left and count <= right:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node

            count += 1
            
        if leftOutOfList:
            leftOutOfList.next = prev  
        else:
            head = prev  

        leftInList.next = curr  

        return head


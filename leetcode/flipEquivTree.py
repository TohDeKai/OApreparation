# https://leetcode.com/problems/flip-equivalent-binary-trees/description/?envType=daily-question&envId=2024-10-24

from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        """
        BFS
        starting at root
        check 
        if left == left and right == right
            then go to left and continue
            then add the other to a queue
            
        if left == right and right == left
            then go to left and continue
            then add the other to a queue (q1,q2 for each of the trees)

        else 
            false
        """
        q1 = deque([root1])
        q2 = deque([root2])

        while q1 and q2:
            curr1 = q1.popleft()
            curr2 = q2.popleft()

            if (curr1 is None) != (curr2 is None):
                return False
            if not curr1 and not curr2:
                continue
            if curr1.val != curr2.val:
                return False
            
            if (self.sameNodes(curr1.left, curr2.left) and self.sameNodes(curr1.right, curr2.right)):
                q1.append(curr1.left)
                q1.append(curr1.right)
                q2.append(curr2.left)
                q2.append(curr2.right)
            elif (self.sameNodes(curr1.left, curr2.right) and self.sameNodes(curr1.right, curr2.left)):
                q1.append(curr1.left)
                q1.append(curr1.right)
                q2.append(curr2.right)
                q2.append(curr2.left)
            else:
                return False

        return len(q1) == len(q2)

    def sameNodes(self, node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
        if not node1 and not node2:
            return True
        if not node1 or not node2:
            return False
        return node1.val == node2.val

# https://leetcode.com/problems/balanced-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def DFS(curr):
            if curr:
                left = DFS(curr.left)
                right = DFS(curr.right)
                if left == -1 or right == -1 or abs(left - right) > 1:
                    return -1
                else:
                    return 1 + max(left, right)
            else:
                return 0

        return DFS(root) != -1

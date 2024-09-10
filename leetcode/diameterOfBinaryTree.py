# https://leetcode.com/problems/diameter-of-binary-tree/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        find height of each node
        maxDepth at each node will be height of left + right node
        """
        res = 0

        def dfs(node):
            nonlocal res
            if node:
                left = dfs(node.left)
                right = dfs(node.right)
                res = max(res, left + right)
                height = 1 + max(left, right)
                return height
            else:
                return 0

        dfs(root)
        return res

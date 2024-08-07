# https://leetcode.com/problems/invert-binary-tree/submissions/1315672127/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None

        left = root.left
        root.left = root.right
        root.right = left

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        def dfs(root):
            if not root:
                return None
            leftTail= dfs(root.left)
            rightTail= dfs(root.right)
            if root.left:
                leftTail.right=root.right
                root.right=root.left
                root.left=None
            last = rightTail or leftTail or root
            return last
        dfs(root)
        
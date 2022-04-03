Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def bfs(a,b):
            if(a==None and b==None):
                return True
            if(a==None or b==None):
                return False
            return (a.val==b.val) and bfs(a.left, b.right) and bfs(a.right, b.left)
        return bfs(root, root)
        
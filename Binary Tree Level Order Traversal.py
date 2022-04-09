Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result=[]
        c=collections.deque()
        c.append(root)
        while c:
            cLen = len(c)
            level = []
            for i in range(cLen):
                node = c.popleft()
                if node:
                    level.append(node.val)
                    c.append(node.left)
                    c.append(node.right)
            if level:
                result.append(level)
        return result
        
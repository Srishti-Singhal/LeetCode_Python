Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def answer(l, r):
            if l>r:
                return None 
            m= (l+r)//2
            root = TreeNode(nums[m])
            root.left = answer(l, m-1)
            root.right = answer(m+1, r)
            return root
        return answer(0, len(nums)-1)
         
            
        
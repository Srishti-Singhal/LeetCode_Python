Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=nums[0]
        r=nums[nums[0]]
        while l!=r:
            l=nums[l]
            r=nums[nums[r]]
        r=0
        while l!=r:
            l=nums[l]
            r=nums[r]
        return l
        
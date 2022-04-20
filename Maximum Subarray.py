Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSub=nums[0]
        curSum=0
        for n in nums:
            if curSum<0:
                curSum=0
            curSum+=n
            maxSub=max(maxSub, curSum)
        return maxSub
                

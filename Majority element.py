Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right= 0,0
        for num in nums:
            if right == 0:
                left = num
                right += 1
            elif num == left:
                right += 1
            else:
                right -= 1
        return left
                
        
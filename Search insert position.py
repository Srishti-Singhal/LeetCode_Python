Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left=0
        right=len(nums) - 1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            elif target>nums[mid]:
                left=mid+1
            else:
                right=mid-1
        return left
        
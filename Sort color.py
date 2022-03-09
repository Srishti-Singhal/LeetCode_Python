Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        result=0
        for _ in range(len(nums)):
            if nums[result]==0:
                nums.pop(result)
                nums.insert(0,0)
                result += 1
            elif nums[result]==2:
                nums.pop(result)
                nums.append(2)
            else:
                result+=1
        return
        
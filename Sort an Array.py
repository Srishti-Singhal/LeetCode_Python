Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums)<=1:
            return nums
        
        mid=len(nums)//2
        left=nums[:mid]
        right=nums[mid:]
        self.sortArray(left)
        self.sortArray(right)
        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                nums[k]=left[i]
                i+=1
            else:
                nums[k]=right[j]
                j+=1
                
            k+=1  
        while i<len(left):
            nums[k]=left[i]
            i+=1
            k+=1
            
        while j<len(right):
            nums[k]=right[j]
            j+=1
            k+=1
        return nums
            

Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l,r=0, len(numbers)-1
        while(l<r):
            total=numbers[l]+numbers[r]
            if total>target:
                r-=1
            elif total<target:
                l+=1
            elif total==target:
                return [l+1, r+1]
        
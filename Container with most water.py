Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height)-1
        result = 0
        while left<right:
            water = (right-left) * min(height[left], height[right])
            if water>result:
                result=water
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return result
        
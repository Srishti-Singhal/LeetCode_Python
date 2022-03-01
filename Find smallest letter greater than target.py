Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        if target >= letters[-1] or target < letters[0]:
            return letters[0]
        l, r = 0, len(letters) - 1
        while l <= r:
            middle = (l+r)//2
            if target >= letters[middle]:
                l = middle + 1
            elif target < letters[middle]:
                r = middle - 1

        if letters[r] <= target:
            return letters[r+1]
        
        else:
            return letters[r]
        
            
        
       
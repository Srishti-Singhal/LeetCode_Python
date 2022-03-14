Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        combination = { ")":"(" , "]":"[" , "}":"{" }
        for i in s:
            if i in combination.values():
                stack.append(i)
            elif stack and combination[i] == stack[-1]:
                stack.pop()
            else:
                return False
        return stack == []
        
        
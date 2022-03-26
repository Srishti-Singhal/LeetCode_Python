Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        add=0
        result=0
        for i in range(0, len(s)):
            if (s[i] == '('):
                add +=1
            else:
                add+=-1
                if(add==-1):
                    result+=1
                    add+=1
        return add+result
                    
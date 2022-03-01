Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        x,i=0,0
        s+=" "
        while i<len(s)-1:
            if s[i]!=' ' and s[i+1]==' ':
                x+=1
            i+=1
        return x
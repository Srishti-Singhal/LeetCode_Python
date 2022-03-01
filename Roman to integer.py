Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        roman = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        n = len(s)
        total = roman[s[n-1]]
        for i in range(n-1,0,-1):
            current = roman[s[i]]
            prev = roman[s[i-1]]
            total += prev if prev >= current else -prev
        return total
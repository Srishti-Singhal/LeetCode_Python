Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        N = len(s)
        S = list(s)
        for i in range(N):
            if S[i] == "(":
                stack.append(i)
            elif S[i] == ")":
                if stack: 
                    stack.pop()
                else:
                    S[i] = ""
        for j in stack:
            S[j] = ""
        return "".join(S)
        
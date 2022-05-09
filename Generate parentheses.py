Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def add_pair(result,s,left,right):
            if left==0 and right ==0:
                result.append(s)
                return
            if right>0:
                add_pair(result,s+ ")", left, right-1)
            if left>0:
                add_pair(result,s+ "(", left-1, right+1)
        result=[]
        add_pair(result, "", n, 0)
        return result
                
Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp=[False]*(len(s)+1)
        dp[len(s)]=True
        for i in range(len(s) -1, -1, -1):
            for j in wordDict:
                if (i+len(j)) <= len(s) and s[i:i+len(j)]==j:
                    dp[i]=dp[i+len(j)]
                if dp[i]:
                    break
        return dp[0]
        
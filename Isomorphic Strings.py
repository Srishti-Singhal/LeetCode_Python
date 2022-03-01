Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hashmap = {}
        for i in range(len(s)):
            if s[i] not in hashmap:
                if t[i] in hashmap.values():
                    return False
                else:
                    hashmap[s[i]] = t[i]
            elif hashmap[s[i]] != t[i]:
                return False
        return True
        
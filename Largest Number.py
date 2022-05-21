Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        def my_sol(x,y):
            aa=str(x)
            bb=str(y)
            aa=aa+bb
            bb=bb+aa
            if aa>bb:
                return -1
            if aa==bb:
                return 0
            if aa<bb:
                return 1
        nums=sorted(nums, cmp=my_sol)
        if nums[0]==0:
            return "0"
        else:
            return "".join([str(n) for n in nums])
        
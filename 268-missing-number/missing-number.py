class Solution(object):
    def missingNumber(self, nums):
        # s=0
        # for i in range(len(nums)):
        #     s+=i
        # return s-sum(nums)
        n=len(nums)
        return n*(n+1)//2-sum(nums)

        
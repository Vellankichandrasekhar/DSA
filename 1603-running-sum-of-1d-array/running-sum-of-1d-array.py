class Solution(object):
    def runningSum(self, nums):
        p=[]
        s=0
        for i in nums:
            s+=i
            p.append(s)
        return p
        
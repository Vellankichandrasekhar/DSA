class Solution(object):
    def majorityElement(self, nums):
        c=0
        e=0
        for i in nums:
            if c==0:
                e=i
            if e==i:
                c+=1
            else:
                c-=1
        return e
        
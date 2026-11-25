class Solution(object):
    def rearrangeArray(self, nums):
        p=[]
        n=[]
        for i in nums:
            if i>0:
                p.append(i)
            else:
                n.append(i)
        res=[]
        for i in range(len(n)):
            res.append(p[i])
            res.append(n[i])
        return res        
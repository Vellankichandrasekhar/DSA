class Solution(object):
    def trap(self, l):
        tw=0
        le,ri=0,len(l)-1
        lm,rm=l[0],l[-1]
        while le<ri:
            if l[le]<l[ri]:
                if l[le]>lm:
                    lm=l[le]
                tw+=(lm-l[le])
                le+=1
            else:
                if l[ri]>rm:
                    rm=l[ri]
                tw+=(rm-l[ri])
                ri-=1
        return tw                

        
        
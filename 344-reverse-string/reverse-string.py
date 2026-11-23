class Solution(object):
    def reverseString(self, s):
        s1=0
        e=len(s)-1
        while s1<e:
            
            s[s1],s[e]=s[e],s[s1]
            s1+=1
            e-=1
        return s
        
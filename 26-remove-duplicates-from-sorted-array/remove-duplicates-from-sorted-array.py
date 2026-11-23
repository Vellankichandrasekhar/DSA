class Solution(object):
    def removeDuplicates(self, nums):
        s=0
        for s2 in range(1,len(nums)):
            if nums[s]!=nums[s2]:
                s+=1

                nums[s]=nums[s2]
        return s+1
        
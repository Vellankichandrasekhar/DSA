class Solution(object):
    def moveZeroes(self, nums):
        ni=0
        for zi in range(0,len(nums)):
            if nums[zi]!=0:
                nums[ni],nums[zi]=nums[zi],nums[ni]
                ni+=1
                
        
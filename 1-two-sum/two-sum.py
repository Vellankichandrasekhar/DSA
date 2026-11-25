# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:

# l=list(map(int,input().split()))        
# k=int(input())
# for i in range(len(l)):
#     for j in range(i,len(l)):
#         if l[i]+l[j]==k:
#             print(i,j)


class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
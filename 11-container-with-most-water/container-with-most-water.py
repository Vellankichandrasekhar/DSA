class Solution(object):
    def maxArea(self, l):
        left = 0
        right = len(l) - 1
        max_area = 0
        while left < right:
            min_height = min(l[left],l[right])
            widht = right - left
            area = min_height * widht
            max_area = max(area, max_area)
            if l[left] < l[right]:
                left += 1
            else:
                right -= 1
        return max_area


        
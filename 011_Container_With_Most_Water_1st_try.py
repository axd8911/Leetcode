'''
93.54%
'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        area = 0
        l = 0
        r = len(height)-1
        
        while l != r:
            temp = min(height[l],height[r]) * (r-l)
            if temp > area:
                area = temp
            
            if height[l] > height[r]:
                r = r - 1
            else:
                l = l + 1
        return area
            

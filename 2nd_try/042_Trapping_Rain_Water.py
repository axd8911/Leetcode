class Solution:
    def trap(self, height: List[int]) -> int:
        left,right = 0,len(height)-1
        leftMax,rightMax = 0,0
        total = 0

        while left < right:
            if height[left] < height[right]:                # if left is shorter, store based on left
                leftMax = max(leftMax,height[left])         # update max height of left
                total += leftMax-height[left]               # add up the storage
                left+=1                                     # this location has been stored or considered, go next
            else:                                           # if right is shorter, or two sides are same, store based on right
                rightMax = max(rightMax,height[right])      # update max height of right
                total += rightMax-height[right]             # add up the storage
                right-=1                                    # move right

        return total

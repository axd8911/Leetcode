class Solution:
    def trap(self, height: List[int]) -> int:
        # 收集左和右的最高点
        #从左边走，收集。左边碰到最高点了，开始收集右边
        count = 0
        
        leftIdx = 0
        rightIdx = len(height)-1
        leftMax,rightMax = 0,0
        
        while leftIdx<=rightIdx:
            if height[leftIdx] < height[rightIdx]:
                leftMax = max(height[leftIdx], leftMax)
                count += leftMax - height[leftIdx]
                leftIdx += 1
                
            else:
                rightMax = max(height[rightIdx], rightMax)
                count += rightMax - height[rightIdx]
                rightIdx -= 1
        return count

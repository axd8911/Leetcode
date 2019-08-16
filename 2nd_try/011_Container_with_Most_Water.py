class Solution:
    def maxArea(self, height: List[int]) -> int:
        #if left is taller,move right
        #if right is taller, move left
        #if they are the same,move both
        #until they meet
        left,right = 0,len(height)-1
        most = 0

        while left <right:
            most = max(most, (right-left)*min(height[left],height[right]))
            #print (left,right,most)
            if height[left] < height[right]:
                for idx in range(left+1,right+1):
                    if height[idx] > height[left]:
                        break
                left = idx

            else:
                for idx in range(right-1,left-1,-1):
                    if height[idx] > height[right]:
                        break
                right = idx

        return most

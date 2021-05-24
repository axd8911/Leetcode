class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        
        horizontalCuts = [0] + horizontalCuts + [h]
        verticalCuts = [0] + verticalCuts + [w]
        
        hDiff, vDiff = [],[]
        
        for i in range(1,len(horizontalCuts)):
            hDiff.append(horizontalCuts[i] - horizontalCuts[i-1])
        for i in range(1,len(verticalCuts)):
            vDiff.append(verticalCuts[i] - verticalCuts[i-1])
        
        return max(hDiff) * max(vDiff)%1000000007

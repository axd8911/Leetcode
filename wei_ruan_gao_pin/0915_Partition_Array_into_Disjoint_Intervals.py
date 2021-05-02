class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        #从左向右开始计数每一位的最大值
        #从右向左开始计数每一位的最小值
        #比较以上两个数列，如果某一位最大值小于等于最小值，那一位就是前部分最后一位
        
        currMax = -float(inf)
        frontMax = []
        currMin = float(inf)
        endMin = []
        
        for i in range(len(A)):
            currMax = max(currMax, A[i])
            frontMax.append(currMax)
        
        for i in range(len(A)-1, -1, -1):
            currMin = min(currMin, A[i])
            endMin.append(currMin)
        
        endMin = endMin[::-1]
        for i in range(len(A)):
            if frontMax[i] <= endMin[i+1]:
                return i+1
            

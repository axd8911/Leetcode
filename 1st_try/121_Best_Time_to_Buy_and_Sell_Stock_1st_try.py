'''
99%
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # we have maxima and minima
        # if new maxima found, compare it to current minimum
        # if new minima found, save it as current minima and wait for next maxima. old maximum expired
        
        if len(prices)==0:
            return 0
        
        best = 0
        minima =prices[0]
        
        for i in range(1,len(prices)-1):
            if prices[i]<=prices[i+1] and prices[i]<=prices[i-1] and prices[i] < minima:
                minima = prices[i]
            elif prices[i]>=prices[i+1] and prices[i]>=prices[i-1]:
                maxima = prices[i]
                if maxima - minima > best:
                     best = maxima - minima
                        
        maxima = prices[-1]
        if maxima - minima > best:
            best = maxima - minima
        
                        
        return best

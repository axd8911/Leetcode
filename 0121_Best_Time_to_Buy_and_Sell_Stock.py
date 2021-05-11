class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #当前最低点和当前值的差
        currMin = float('inf')
        res = 0
        for item in prices:
            currMin = min(currMin,item)
            res = max(res, item-currMin)
        return res

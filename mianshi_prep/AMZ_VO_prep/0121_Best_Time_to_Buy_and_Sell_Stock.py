class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # update the lowest till now
        if not prices:
            return 0
        lowest = prices[0]
        profit = 0
        for item in prices:
            lowest = min(lowest,item)
            profit = max(profit, item-lowest)
        return max(profit,0)

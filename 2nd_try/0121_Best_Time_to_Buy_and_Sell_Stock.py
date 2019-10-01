class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #from left to right,calculate the difference between curr and appeared minumum
        if not prices:
            return 0


        largest = 0
        minimum = prices[0]

        for item in prices:
            largest = max(largest,item-minimum)
            minimum = min(item,minimum)

        return largest
                          

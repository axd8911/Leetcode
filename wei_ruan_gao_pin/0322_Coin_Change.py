class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #bottom up
        coins.sort()
        count = {}
        count[0]=0
        for i in range(amount+1):
            if i in count:
                for coin in coins:
                    count[i+coin] = min(count[i+coin], count[i]+1) if i+coin in count else count[i]+1
        return count[amount] if amount in count else -1

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.res = float('inf')
        coins.sort(reverse=True)
        length = len(coins)

        def dfs(idx,rem,cnt):
            if not rem:
                self.res = min(self.res,cnt)

            for i in range(idx,length):
                if coins[i]<=rem<coins[i]*(self.res-cnt):
                    dfs(i,rem-coins[i],cnt+1)

        for i in range(length):
            dfs(i,amount,0)

        return self.res if self.res!=float('inf') else -1

class Solution:
    def countArrangement(self, N: int) -> int:
        memo = {}
        def helper(idx, res):
            if idx == 1:
                return 1
            key = (idx,res)
            if key in memo:
                return memo[key]
            total = 0
            for j in range(len(res)):
                if not res[j]%idx or not idx%res[j]:
                    total += helper(idx-1,res[:j]+res[j+1:])
            memo[key] = total
            return total
        return helper(N,tuple(range(1,N+1)))

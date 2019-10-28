class Solution:
    def numWays(self, n: int, k: int) -> int:

        if n==0:
            return 0
        if n==1:
            return k

        same = [k]
        diff = [k*(k-1)]

        for i in range(2,n):
            sameToDiff = same[-1] * (k-1)
            diffToDiff = diff[-1] *(k-1)
            diffToSame = diff[-1] * 1

            same.append(diffToSame)
            diff.append(sameToDiff + diffToDiff)

        return same[-1] + diff[-1]

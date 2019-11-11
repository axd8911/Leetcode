class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        res = [0 for i in range(N+1)]

        for x,y in trust:
            res[x] -= 1
            res[y] += 1

        for i in range(1,len(res)):
            if res[i] == N-1:
                return i
        return -1

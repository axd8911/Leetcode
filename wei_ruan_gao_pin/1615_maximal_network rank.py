class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        #这题是问，到达两个city的最多有多少条路
        #一维：有几条路联通这个城市
        #二维：每两个城市之间有没有通路
        
        roadSet = set((a,b) for a,b in roads)
        roadCount = [0 for i in range(n)]
        for a,b in roadSet:
            roadCount[a] += 1
            roadCount[b] += 1
        
        
        maximum = 0
        repeat = 0
        
        for i in range(n):
            for j in range(i+1,n):
                repeat = 0
                if i==j:
                    continue
                if (i,j) in roadSet or (j,i) in roadSet:
                    repeat = 1
                
                maximum = max(maximum, roadCount[i] + roadCount[j] - repeat)
        return maximum

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = collections.defaultdict(set)
        for a,b in roads:
            graph[a].add(b)
            graph[b].add(a)
            
        maximum = 0
        for i in range(n):
            for j in range(i+1,n):
                if j in graph[i]:
                    repeat = 1
                else:
                    repeat = 0
                maximum = max(maximum, len(graph[i]) + len(graph[j]) - repeat)
        return maximum

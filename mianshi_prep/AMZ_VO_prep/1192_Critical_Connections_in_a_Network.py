class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        dic = collections.defaultdict(list)
        for x,y in connections:
            dic[x].append(y)
            dic[y].append(x)

        parent = [-1] * n
        low = [float('inf')] * n
        disc = [float('inf')] * n
        visited = [False] * n
        res = []
        self.appear = 0

        def helper(i,parent,low,disc,visited):
            visited[i] = True
            low[i] = self.appear
            disc[i] = self.appear
            self.appear += 1

            for j in dic[i]:
                if not visited[j]:
                    parent[j] = i
                    helper(j,parent,low,disc,visited)
                    low[i] = min(low[i],low[j])

                    if low[j]>disc[i]:
                        res.append(sorted([i,j]))

                elif j != parent[i]:
                    low[i] = min(low[i],disc[j])

        helper(0,parent,low,disc,visited)
        return res


                

class Solution:
    def travelingIsFun(n,g,originCities,destinationCities):
        parent = [range(n+1)]
        rank = [0] * (n+1)

        def find(item):
            if item != parent[item]:
                parent[item] = find(parent[item])
            return parent[item]

        def union(a,b):
            a = find(a)
            b = find(b)
            if a != b:
                if rank[a] < rank[b]:
                    parent[a] = b
                else:
                    parent[b] = a
                    rank[a] += rank[a] == rank[b]

        for i in range(g+1,n+1):
            factor = 2
            while factor * i <= n+1:
                union(i * factor, i)
                factor += 1

        output = []

        for i in range(len(originCities)):
            if find(originCities[i]) == find(destinationCities[i]):
                output.append(1)
            else:
                output.append(0)

        return output

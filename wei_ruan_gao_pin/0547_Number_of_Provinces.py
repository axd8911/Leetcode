class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        connections = collections.defaultdict(set)
        
        for i in range(len(isConnected)):
            for j in range(i+1,len(isConnected[0])):
                if isConnected[i][j] == 1:
                    connections[i].add(j)
                    connections[j].add(i)
        visited = set()
        
        def helper(city):
            curr = collections.deque([city])
            while curr:
                temp = curr.popleft()
                for item in connections[temp]:
                    if item not in visited:
                        visited.add(item)
                        curr.append(item)
        
        count = 0
        for i in range(len(isConnected)):
            if i not in visited:
                count += 1
                helper(i)
        return count

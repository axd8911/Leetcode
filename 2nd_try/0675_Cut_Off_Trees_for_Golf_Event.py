class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        order = []
        h = len(forest)
        w = len(forest[0])
        step = 0
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        def BFS(past,curr):
            visited = set()
            visited.add(past)
            queue = collections.deque([past])
            step = 0
            while queue:
                #print (visited)
                step += 1
                length = len(queue)
                for i in range(length):
                    x,y = queue.popleft()
                    for dx,dy in directions:
                        nx,ny = x+dx,y+dy
                        if (nx,ny) == curr:
                            return step
                        if 0<=nx<h and 0<=ny<w and forest[nx][ny]!=0 and (nx,ny) not in visited:
                            visited.add((nx,ny))
                            queue.append((nx,ny))
            return -1
 
        for i in range(h):
            for j in range(w):
                if forest[i][j]>1:
                    heapq.heappush(order,[forest[i][j],i,j])

        past = tuple((0,0))
        init = heapq.nsmallest(1,order)
        #print (init)
        if (init[0][1],init[0][2]) == (0,0):
            heapq.heappop(order)

        while order:
            temp = heapq.heappop(order)
            curr = tuple((temp[1],temp[2]))
            add = BFS(past,curr)
            #print (past,curr,add)
            if add == -1:
                return -1
            step += add
            past = curr

        return step

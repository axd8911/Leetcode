class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        lenX = len(grid)
        lenY = len(grid[0])
        visited = set()
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        count = 0
        
        def bfs(x,y):
            curr = collections.deque([(x,y)])
            while curr:
                currX, currY = curr.popleft()
                for dx,dy in directions:
                    newX = currX +dx
                    newY = currY + dy
                    if 0<=newX<lenX and 0<=newY<lenY and (newX,newY) not in visited and grid[newX][newY] == '1':
                        visited.add((newX,newY))
                        curr.append((newX,newY))
        
        for i in range(lenX):
            for j in range(lenY):
                if grid[i][j]=='1' and (i,j) not in visited:
                    count += 1
                    bfs(i,j)
        return count

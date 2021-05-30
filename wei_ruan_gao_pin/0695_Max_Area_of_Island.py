class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        direction = [[1,0],[-1,0],[0,1],[0,-1]]
        visited = set()
        maximum = 0
        
        def bfs(x,y):
            area = 1
            curr = collections.deque([(x,y)])
            while curr:
                curr_x,curr_y = curr.pop()
                for dx,dy in direction:
                    new_x = curr_x+dx
                    new_y = curr_y+dy
                    if 0<=new_x<row and 0<=new_y<col and grid[new_x][new_y]==1 and (new_x,new_y) not in visited:
                        area+=1
                        visited.add((new_x,new_y))
                        curr.append((new_x,new_y))
            return area
        
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1 and (i,j) not in visited:
                    visited.add((i,j))
                    maximum = max(maximum, bfs(i,j))
        return maximum

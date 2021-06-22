class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # BFS: collect all rotted oranges as start
        # collect all fresh oranges at the beginning
        # create a visited. If any fresh not in oranges, return -1. Else return steps
        
        rotted = collections.deque([])
        fresh = []
        visited = set()
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    fresh.append((i,j))
                if grid[i][j] == 2:
                    rotted.append((i,j))
                    visited.add((i,j))
        step = 0
        while True:
            length = len(rotted)
            for i in range(length):
                x,y = rotted.popleft()
                for dx,dy in directions:
                    if 0<=x+dx<len(grid) and 0<=y+dy<len(grid[0]) and grid[x+dx][y+dy]==1 and (x+dx,y+dy) not in visited:
                        visited.add((x+dx,y+dy))
                        rotted.append((x+dx,y+dy))
            if not rotted:
                break
            step += 1
        for item in fresh:
            if item not in visited:
                return -1
        return step

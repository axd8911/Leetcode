class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # DP and BFS
        # if top-left or bottom-right is not 0, return -1
        # save dict. if a neighbor not in dict or its value is larger, update its value and append it for next

        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        dic = {(0,0):1}
        h = len(grid)
        queue = collections.deque([(0,0)])
        dic[(0,0)] = 1
        directions = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]

        while queue:
            if (h-1,h-1) in dic:
                return dic[(h-1,h-1)]
            x,y = queue.popleft()
            for dx,dy in directions:
                nx,ny =x+dx,y+dy
                if 0<=nx<h and 0<=ny<h and grid[nx][ny] == 0 and (nx,ny) not in dic:

                    dic[(nx,ny)] = dic[(x,y)] + 1
                    queue.append((nx,ny))

        return -1
        

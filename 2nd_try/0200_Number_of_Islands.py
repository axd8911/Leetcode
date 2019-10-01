
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        h = len(grid)
        w = len(grid[0])

        visited = [[False for _ in range(w)] for _ in range(h)]
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        def island1(row,col):                        # this is recursive DFS
            #print (visited)
            if row<0 or row>=h or col<0 or col>=w or grid[row][col]=='0' or visited[row][col]:
                #print ('a')
                return
            visited[row][col]=True
            island(row+1,col) or island(row-1,col) or island(row,col+1) or island(row,col-1)
            #return visited

        def island2(row,col):                       # this is stack DFS
            stack = [(row,col)]
            while stack:
                x,y = stack.pop()
                for dx,dy in directions:
                    if 0<=x+dx<h and 0<=y+dy<w and not visited[x+dx][y+dy] and grid[x+dx][y+dy]=='1':
                        stack.append((x+dx,y+dy))
                        visited[x+dx][y+dy] = True

        cnt = 0
        for i in range(h):
            for j in range(w):
                #print (i,j)
                if not visited[i][j] and grid[i][j] == '1':
                    #visited[i][j]=True
                    cnt+=1
                    island(i,j)
                    #print (visited)
        return cnt

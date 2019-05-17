'''
92.35%

Very similar way as 063. Accumulate values from previous grids

'''



class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        x, y = len(grid[0]), len(grid)
        
        for i in range(1,x):
            grid[0][i] = grid[0][i-1] + grid[0][i]
        for i in range(1,y):
            grid[i][0] = grid[i-1][0] + grid[i][0]
            
        for i in range(1,y):
            for j in range(1,x):
                grid[i][j] = min(grid[i-1][j],grid[i][j-1]) + grid[i][j]
                
        return grid[-1][-1]
        

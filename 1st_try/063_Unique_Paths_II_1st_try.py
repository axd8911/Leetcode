'''
96.9%

Checked solution before getting the correct solution. Need to redo it and memorize the theory.
'''

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        if obstacleGrid[0][0] == 1:
            return 0
        
        verti,hori = len(obstacleGrid),len(obstacleGrid[0])
        
        for i in range(0,hori):
            if obstacleGrid[0][i] == 0:
                obstacleGrid[0][i] = 1
            else:
                obstacleGrid[0][i:] = [0] * (hori-i)
                break
    
        for i in range(1,verti):
            if obstacleGrid[i][0] == 0:
                obstacleGrid[i][0] = 1
            else:
                for j in range(i,verti):
                    obstacleGrid[j][0] = 0
                break
                        
        for i in range(1,verti):
            for j in range(1,hori):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else: obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
                       
        return obstacleGrid[-1][-1]
        
    

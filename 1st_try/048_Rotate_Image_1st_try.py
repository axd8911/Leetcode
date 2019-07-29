'''
62%

Two solutions below are almost the same, one of them is compacted to one line
The multiple lines solution is helpful to understand the process

Comments:
1. It is important to disconnect the relation between variables (matrix2 and matrix)
2. The art of loop lists in list in one line
'''

#solution 1
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix[:] = [[matrix[len(matrix)-1-y][x] for y in range(len(matrix))] for x in range(len(matrix))]


#solution 2

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        d = len(matrix)
        matrix2 = [[matrix[x][y] for y in range(d)] for x in range(d)]
        
        for i in range(d):
            for j in range(d):
                matrix[i][j] = matrix2[d-1-j][i]
          
        

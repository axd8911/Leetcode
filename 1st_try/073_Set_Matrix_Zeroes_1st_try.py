'''
93.95%

Constant space achieved. 88%
'''


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        x = []
        y = []
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    if j not in x: x.append(j)
                    if i not in y: y.append(i)
                    
        for item in x:
            for i in range(len(matrix)):
                matrix[i][item] = 0
        for item in y:
            for i in range(len(matrix[0])):
                matrix[item][i] = 0

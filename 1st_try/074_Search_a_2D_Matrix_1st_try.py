'''
99.42%

Make sure to cover all special cases.
'''


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix == []:
            return False
        
        while len(matrix) > 1:
            loc = len(matrix)//2
            if matrix[loc][0] > target:
                matrix = matrix[:loc]
            elif matrix[loc][0] < target:
                matrix = matrix[loc:]
            else:
                return True
        
        matrix = matrix[0]
        
        while matrix:
            loc = len(matrix)//2
            if matrix[loc] > target:
                matrix = matrix[:loc]
            elif matrix[loc] < target:
                matrix = matrix[loc+1:]
            else: return True
            
        return False
                
        

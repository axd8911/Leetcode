'''
98.5%
How people will lopp over such matrix, do the same

'''


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        output = []
        
        while matrix != []:
            output = output + matrix.pop(0)
            if matrix == []: break
                
            right = []
            for i in range(len(matrix)):
                right.append(matrix[i].pop())
            output = output + right
            if matrix[i] == []: break
                
            output = output + matrix.pop()[::-1]
            if matrix == []: break
            
            left = []
            for i in range(len(matrix)):
                print(matrix)
                left.append(matrix[i].pop(0))
            output = output + left[::-1]
            if matrix[i] == []: break
            
        return output

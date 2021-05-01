class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        up = 0
        down = len(matrix)-1
        left = 0
        right = len(matrix[0])-1
        
        res = []
        
        while True:
            if up<=down:
                res += matrix[up][left:right+1]
                up += 1
            if left<=right:
                res += [matrix[item][right] for item in range(up,down+1)]
                right -= 1
            if up<=down:
                res += matrix[down][left:right+1][::-1]
                down -= 1
            if left <= right:
                res += [matrix[item][left] for item in range(up,down+1)][::-1]
                left += 1
            if left > right and up > down:
                break
        return res

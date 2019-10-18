class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # search from len,0, if target is bigger, 0 moves to right, else 0 moves up


        x = len(matrix)-1
        y = 0
        while 0<=x<len(matrix) and 0<=y<len(matrix[0]):
            if matrix[x][y] == target:
                return True
            if matrix[x][y] >target:
                x-=1
            else:
                y+=1
        return False

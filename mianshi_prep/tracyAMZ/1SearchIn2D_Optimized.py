 class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        d1 = len(matrix)-1
        d2 = 0
        while d1>=0 and d2<len(matrix[0]):
            if matrix[d1][d2] == target:
                return True
            if matrix[d1][d2] < target:
                d2 += 1
            else:
                d1 -= 1
        return False

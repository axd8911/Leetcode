class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        if not matrix or not matrix[0]:
            return False


        row = len(matrix)
        col = len(matrix[0])

        i,j = 0, col-1
        for i in range(row):
            j = col - 1
            if matrix[i][j] < target:
                continue
            else:
                while j>=0:
                    print (i,j)
                    if matrix[i][j] == target:
                        return True

                    j -= 1
        return False

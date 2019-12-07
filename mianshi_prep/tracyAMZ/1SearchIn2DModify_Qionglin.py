class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        if not matrix or not matrix[0]:
            return False                            # this initial corner case may be necessary


        row = len(matrix)
        col = len(matrix[0])

        i,j = 0, col-1
        for i in range(row):
            # j = col - 1                           I grey out this line. No need to update j in each row!!!!!!!!!!!!!
            if matrix[i][j] < target:
                continue
            else:
                while j>=0 and matrix[i][j] - target >=0:           # I added another condition here, so that as long as current number becomes smaller than target, go to next line
                    if matrix[i][j] == target:
                        return True

                    j -= 1
        return False

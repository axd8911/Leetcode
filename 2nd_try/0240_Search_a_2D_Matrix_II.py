class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        d1 = len(matrix)-1
        d2 = 0

        while True:
            if d1<0 or d2>=len(matrix[0]):
                return False
            if matrix[d1][d2] == target:
                return True


            if matrix[d1][d2] < target:
                d2+=1
            else:
                d1-=1

        

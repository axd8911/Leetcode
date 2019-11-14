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


# binary search, which is not a good always
class Solution:


    def binarySearch(self,matrix,target,start,vertical):
        low = start
        high = len(matrix[0])-1 if vertical else len(matrix)-1

        while low<=high:
            mid = (low+high)//2
            if vertical:
                print ('vertical ', start, mid, matrix[start][mid])
                if matrix[start][mid]==target:
                    return True
                if matrix[start][mid]>target:
                    high = mid-1
                else:
                    low = mid+1
            else:
                print ('horizontal ', start, mid, matrix[mid][start])
                if matrix[mid][start]==target:
                    return True
                if matrix[mid][start]>target:
                    high = mid-1
                else:low = mid+1
        return False

    def searchMatrix(self, matrix,target):
        if not matrix:
            return False

        for i in range(min(len(matrix),len(matrix[0]))):
            vertical = self.binarySearch(matrix,target,i,True)
            horizontal = self.binarySearch(matrix,target,i,False)
            if vertical or horizontal:
                return True
        return False

    

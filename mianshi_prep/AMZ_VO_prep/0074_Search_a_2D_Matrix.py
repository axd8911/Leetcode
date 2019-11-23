class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        h,w = len(matrix),len(matrix[0])
        l1,r1 = 0,h-1
        l2,r2 = 0,w-1
        found = False

        while l1<=r1:
            mid = (l1+r1)//2
            if matrix[mid][0]<=target<=matrix[mid][-1]:
                col = mid
                found = True
                break
            if matrix[mid][0]>target:
                r1 = mid - 1
            else:
                l1 = mid + 1

        if not found:
            return False

        while l2<=r2:
            mid = (l2+r2)//2
            if matrix[col][mid] == target:
                return True
            if matrix[col][mid] > target:
                r2 = mid - 1
            else:
                l2 = mid + 1
        return False

class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        start, end = 1,len(A)-1
        while start<=end:
            mid = (start+end)//2
            if A[mid-1]<A[mid] and A[mid]>A[mid+1]:
                return mid
            if A[mid]<A[mid+1]:
                start = mid + 1
            elif A[mid]<A[mid-1]:
                end = mid - 1

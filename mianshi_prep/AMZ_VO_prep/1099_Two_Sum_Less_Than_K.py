class Solution(object):
    def twoSumLessThanK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        maximum = -1
        A.sort()
        l,r = 0,len(A)-1
        while l<r:
            if A[l]+A[r]>=K:
                r-=1
            else:
                maximum = max(maximum,A[l]+A[r])
                l+=1


        return maximum

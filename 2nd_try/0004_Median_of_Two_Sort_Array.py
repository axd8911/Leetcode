class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m,n = len(nums1),len(nums2)
        if m>n:
            nums1,nums2,m,n = nums2,nums1,n,m
        total = m+n
        apart = (total+1)//2
        start,end = 0,m
        while start<=end:
            mid1= (start+end)//2
            mid2= apart-mid1
            if mid1-1>=0 and nums1[mid1-1]>nums2[mid2]:
                end = mid1-1
            elif mid1<m and nums2[mid2-1]>nums1[mid1]:
                start =mid1+1
            else:
                if mid1==0:left = nums2[mid2-1]
                elif mid2==0:left = nums1[mid1-1]
                else:left = max(nums1[mid1-1],nums2[mid2-1])
                if total%2==1:
                    return left
                if mid1==m:right = nums2[mid2]
                elif mid2==n:right = nums1[mid1]
                else: right = min(nums1[mid1],nums2[mid2])
                return (left+right)/2

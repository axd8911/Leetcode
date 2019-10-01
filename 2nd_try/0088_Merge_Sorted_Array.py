class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        loc1,loc2 = m-1,n-1
        idx = 1

        while loc1>=0 and loc2>=0:
            if nums1[loc1] > nums2[loc2]:
                nums1[m+n-idx] = nums1[loc1]
                loc1-=1
            else:
                nums1[m+n-idx] = nums2[loc2]
                loc2-=1
            idx+=1

        if loc2 >=0:
            nums1[:loc2+1] = nums2[:loc2+1]

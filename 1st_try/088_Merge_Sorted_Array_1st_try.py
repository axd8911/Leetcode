'''
99.93%

'''


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """        
        m0 = 0
        
        nums1[:] = nums1[:m]
        
        while True:
            if nums2 == []:
                break
            if m0 == len(nums1):
                nums1[:] = nums1 + nums2
                break
                
            if nums1[m0] <= nums2[0]:
                m0 = m0 + 1
            else:
                nums1.insert(m0,nums2.pop(0))
                m0 = m0 + 1

                

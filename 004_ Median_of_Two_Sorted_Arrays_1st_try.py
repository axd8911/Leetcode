'''
Run time matches requirement
It is still a one by one removing process - piece by piece removing is my next goal

46%
'''

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        
        length = len(nums1) + len(nums2)
        length1 = len(nums1)
        length2 = len(nums2)
        if length%2 == 0:
            total_trim = length/2 - 1
        else:
            total_trim = (length - 1)/2
        
        left = length - total_trim
        #print (nums1,nums2,total_trim)    
        if len(nums1) > len(nums2):
            nums1 = nums1[int(len(nums1)-left):]
            total_trim = total_trim - length1 + left
            #print(len(nums1)-left)
        if len(nums2) > len(nums1):
            nums2 = nums2[int(len(nums2)-left):]
            total_trim = total_trim - length2 + left
          
        #print (nums1,nums2,total_trim)        
        while total_trim != 0 and len(nums1)>0 and len(nums2)>0:
            if nums1[0] <= nums2[0]:
                nums1.pop(0)
                total_trim = total_trim - 1
            else:
                nums2.pop(0)
                total_trim = total_trim - 1
        #print (nums1,nums2,total_trim)  
            
        if length%2 == 0:
            return sum(sorted(nums1+nums2)[0:2])/2
                
        if length%2 == 1 and len(nums1) == 0:
            return nums2[0]
        
        if length%2 == 1 and len(nums2) == 0:
            return nums1[0]        
        
        else:
            #print (nums1,nums2)
            return min(nums1[0], nums2[0])
        
        
        
        

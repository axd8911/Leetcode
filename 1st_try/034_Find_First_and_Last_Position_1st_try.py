'''
87%
Binary search. Try to practise binary search.


'''

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        nums2 = nums
        goodPos = -1
        cnt = 0
        while nums2:
            pos = len(nums2)//2
            if nums2[pos] > target:
                nums2 = nums2[:pos]
            elif nums2[pos] < target:
                cnt = cnt + pos + 1
                nums2 = nums2[pos+1:]
            elif nums2[pos] == target:
                goodPos = pos + cnt
                break
        
        if goodPos == -1:
            return [-1,-1]
        
        minVal = goodPos
        maxVal = goodPos
        while minVal != 0:
            if nums[minVal] == nums[minVal-1]:
                minVal = minVal - 1
            else:
                break

        while maxVal != len(nums) - 1:
            if nums[maxVal] == nums[maxVal+1]:
                maxVal = maxVal + 1
            else:
                 break
                        
        return [minVal,maxVal]
        

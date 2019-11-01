class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start,end = 0,len(nums)-1

        if not nums or len(nums)==1:
            return 0

        if nums[0]>nums[1]:
            return 0
        if nums[-1]>nums[-2]:
            return len(nums)-1

        while start<=end:
            mid = (start+end)//2
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid
            if nums[mid]<nums[mid-1]:
                end = mid -1
            else:
                start = mid + 1

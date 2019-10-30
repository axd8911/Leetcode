class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return
        if nums[0]<=nums[-1]:
            return nums[0]

        start,end = 1,len(nums)-1
        while start <= end:
            mid = (start+end)//2

            if nums[mid] < nums[mid-1]:
                return nums[mid]
            if nums[mid] > nums[0]:
                start = mid + 1
            else:
                end = mid - 1

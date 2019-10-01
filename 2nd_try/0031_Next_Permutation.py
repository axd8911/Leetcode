class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        change = False

        for i in range(len(nums)-2,-1,-1):
            if nums[i] < nums[i+1]:
                start = i+1
                change = True
                break
        if not change:
            nums[:] = nums[::-1]

        else:
            location = i
            start,end = i+1,len(nums)-1
            while start<=end:
                mid = (start+end)//2
                if nums[i]<nums[mid] and (mid+1>=len(nums) or nums[i]>=nums[mid+1]):
                    break
                if nums[mid] <= nums[i]:
                    end = mid-1
                else:
                    start = mid+1

            nums[mid],nums[i] = nums[i],nums[mid]
            nums[i+1:len(nums)] = nums[len(nums)-1:i:-1]

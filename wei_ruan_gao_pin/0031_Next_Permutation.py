class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """        
        found = False
        
        def findLarger(nums, target):
            if target > nums[-1]:
                return len(nums)
            if nums[0] > target:
                return 0
            
            l = 0
            r = len(nums)-1
            while l<=r:
                mid = (l+r)//2
                if nums[mid]>target and nums[mid-1]<=target:
                    return mid
                if nums[mid]<=target:
                    l=mid+1
                else:
                    r=mid-1
        
        for i in range(len(nums)-2,-1,-1):
            if nums[i] < nums[i+1]:
                found = True
                nums[i+1:] = sorted(nums[i+1:])
                idx = findLarger(nums[i+1:],nums[i])
                if idx!=len(nums[i+1:]):
                    nums[i],nums[idx+i+1]=nums[idx+i+1],nums[i]
                break
                
        if not found:
            nums[:] = nums[::-1]        

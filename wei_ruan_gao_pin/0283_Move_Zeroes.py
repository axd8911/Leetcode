class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # when meet a non-0, move it to current index
        curr = 0
        for i in range(len (nums)):
            if nums[i]!=0:
                nums[i],nums[curr]=nums[curr],nums[i]
                curr+=1
        return nums

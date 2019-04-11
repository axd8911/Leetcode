'''
93%
Search that by half, O(log n)
'''


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        if target > nums[-1]:
            return len(nums)
        
        if target <= nums[0]:
            return 0
        
        n = -(-(len(nums))//2)
        mover = -(-len(nums)//2)

        while target != nums[n] and mover != 0:
            mover = -(-mover//2)
            if target > nums[n] and target < nums[n+1]:
                return n + 1
            if target > nums[n]:
                n = n + mover
            else:
                n = n - mover
        
        return n

'''
40%
No new list is generated, as required by the problem.

Another method could slightly improve the run time: for loop, directly overwrite next unrepeated value to the list, until all the list are checked 
'''


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = 0
        while n < len(nums)-1:
            if nums[n] == nums[n+1]:
                del nums[n]
            else: n += 1   
        return len(nums)

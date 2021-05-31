class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # index 0 to len-1 should map to number 1 to len. We should check from 1 to length by marking index 0 to len-1
        # if in each index, the number <=0, it is not counted. Make it 0. 0 will not be counted.
        # if in each index, it has a number 1 to len, then mark it to the corresponding location (make it negative)
        for i in range(len(nums)):
            if nums[i]<0:
                nums[i]=0
        for i in range(len(nums)):
            mapping = abs(nums[i])-1
            if mapping>=0 and mapping<len(nums):
                if nums[mapping]==0:
                    nums[mapping]=-inf
                elif nums[mapping]>0:
                    nums[mapping]*=-1
        for i in range(len(nums)):
            if nums[i]>=0:
                return i+1
        return len(nums)+1

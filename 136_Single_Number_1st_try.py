'''
Two approaches below. One is faster but created new set. Run time O(n), 70%
The other one is slow but just work on the list itself. Run time n**2, less memory
'''

# solution1
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return sum(set(nums)) * 2 - sum(nums)
        
# solution2
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        n = 1
        while n < len(nums):
            if nums[n] not in nums[:n]:
                n = n + 1
            else:
                nums.remove(nums[n])
                del nums[n-1]
                n = n - 1 
        return nums[0]

'''
65%

Feel free to overwrite later items to eariler index because eariler index will never be used in the future
Almost the same as #026
'''



class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = 0
        for item in nums:
            if item != val:
                nums[n] = item
                n = n + 1
                
                
        return len(nums[:n])

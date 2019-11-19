class Solution:
    def find132pattern(self, nums: List[int]) -> bool:

        if len(nums)<=2:
            return False

        minVal = nums[0]
        mini = [minVal]
        for item in nums:
            mini.append(min(mini[-1],item))
        stack = []

        for i in range(len(nums)-1,-1,-1):
            if nums[i]>mini[i]:
                while stack and stack[-1]<=mini[i]:
                    stack.pop() # delete the numbers that will never be used in the future
                if stack and stack[-1]<nums[i]:
                    return True
                stack.append(nums[i])
        return False

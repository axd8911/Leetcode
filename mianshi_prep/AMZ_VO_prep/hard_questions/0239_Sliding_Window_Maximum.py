class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []

        window = collections.deque()
        output = []

        for i in range(len(nums)):
            if window and window[0]<=i-k:
                window.popleft()
            while window and nums[window[-1]]<nums[i]:
                window.pop()
            window.append(i)
            if i>=k-1:
                output.append(nums[window[0]])
        return output

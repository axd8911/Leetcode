'''
99%
'''

# 从0或1开始，如果从0开始，剩下的要从2开始，如果从1开始，剩下的要从3开始
# 不妨这么想：求截至某个位置的最大值：如果上一个位置已经到末尾，那要比较（再前一个位置的max加此位置）和上一个位置；如果上一个位置没到末尾，这个就直接加该位置值

class Solution:
    def rob(self, nums: List[int]) -> int:
        self.maximum = 0
        
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0],nums[1])
        
        big = []
        big.append(nums[0])
        big.append(max(nums[0],nums[1]))
        
        for i in range(2,len(nums)):
            if nums[i] + big[i-2] > big[i-1]:
                big.append(nums[i] + big[i-2])
            else:
                big.append(big[i-1])
                
        return big[-1]

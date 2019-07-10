class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        #从前刷到后，加到超过s，记录位数
        #减去最前位，直到小于s
        #一直向后叠加，超过s就开始减去前面的，小于s就记录刚刚的位数
        
        start_idx = 0
        total = 0
        smallest = len(nums)
        
        check = False
        
        for i in range(len(nums)):
            total += nums[i]
            if total >= s:
                check = True
                while total >= s:
                    total -= nums[start_idx]
                    start_idx += 1
                    if total < s:
                        break
                    
                    
                if i - start_idx + 2 < smallest:
                    smallest = i - start_idx + 2
                if smallest == 1:
                    return 1
        
        if not check:
            return 0
        else:
            return smallest
                
            

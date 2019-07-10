class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #如果当前数字大于tail最后一个，那就把这个值append给tail
        #如果当前数字在小于最后一个数，那就替代掉刚好比他大的那个数
        
        if not nums:
            return 0
        
        tails = [nums[0]]
        idx=0
        for item in nums:
            
            if item > tails[-1]:
                tails.append(item)
                
            elif item < tails[-1]:
                temp = tails
                idx = 0
                while True:
                    length = len(temp)
                    #不要瞎写：我们要找的是那个刚好大于当前值的数字的位置
                    #如果当前值小于中间值，那就删掉包括中间值和后面所有的
                    #如果当前值大于中间值，那就删掉包括中间值和前面所有的
                    #如果相等，跳出当前while不变化
                    
                    if item == temp[length//2]:
                        break
                    
                    elif item < temp[length//2]:
                        temp = temp[:length//2]
                    else:
                        idx += length//2+1
                        temp = temp[length//2+1:]
                    if len(temp) < 1:
                        tails[idx] = item
                        break
                
            #print (tails)

        return len(tails)
                        

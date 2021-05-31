class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        
        time = [item%60 for item in time]
        count_zero = 0
        for item in time:
            if item == 0:
                count_zero += 1
        total = count_zero*(count_zero-1)//2
        dic = collections.defaultdict(int)
        for item in time:
            total += dic[60-item]
            dic[item]+=1
        return total
            
        

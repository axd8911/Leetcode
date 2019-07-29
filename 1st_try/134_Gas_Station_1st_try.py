'''
98%
This is almost the same as another one (largest sum in list)
'''


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        gain = []
        for i in range(len(gas)):
            gain.append(gas[i]-cost[i])
        
        dgain = gain + gain
        
        sumup = 0
        n = 0
        flag = 0
        for i in range(len(dgain)):
            sumup += dgain[i]
            n = n + 1
            if sumup<0:
                sumup = 0
                flag = i+1
                n = 0
                
            if n == len(gain):
                return flag
            
        return -1

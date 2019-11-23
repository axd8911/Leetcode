class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # from which index, sum of gas is always bigger than sum of cost
        # record the start point. if becomes negative, move the start

        start = 0
        total = 0
        diff = [item1-item2 for item1,item2 in zip(gas,cost)] * 2
        print (diff)

        for i in range(len(diff)):
            total += diff[i]
            while total < 0:
                total -= diff[start]
                start += 1

        return start if start <len(gas) else -1

        

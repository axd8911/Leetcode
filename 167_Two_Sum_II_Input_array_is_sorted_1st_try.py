class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers)-1
        
        while start < end:
            result = numbers[start] + numbers[end]
            if result > target:
                end = end - 1
            elif result < target:
                start = start + 1
            else:
                return [start+1,end+1]
            

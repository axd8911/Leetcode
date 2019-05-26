'''
77%
O(m n^2)
'''


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        twoSum = {}
        nums.sort()
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] in twoSum:
                    twoSum[nums[i]+nums[j]].append((i,j))
                else:
                    twoSum[nums[i]+nums[j]] = [(i,j)]
                    
        result = set()
        
        for key in twoSum:
            value = target - key
            if value in twoSum:
                set1 = twoSum[key]
                set2 = twoSum[value]
                for i1,i2 in set1:
                    for i3,i4 in set2:
                        if i1!=i3 and i1!=i4 and i2!=i3 and i2!=i4:
                            newitem = sorted([nums[i1],nums[i2],nums[i3],nums[i4]])
                            result.add(tuple(newitem))
                            
        return list(result)

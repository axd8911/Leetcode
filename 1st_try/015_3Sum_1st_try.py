'''
Leetcode score:89.1%
Storage: 17% but within main range
Run time (n**2)

Comments:
1. This is fast enough.
2. Should make good use of sorting: reduce unnecessary loop items
3. worth another try without seeing old code: can I remember what I did?
4. To achieve 3, it worth more practice in similar problems
5. #REPEATATION MAKES PERFECT#

'''


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(0,len(nums)-2):
            if nums[i] > 0:
                break            
            
            if i > 0 and nums[i] == nums[i-1]:
                continue

            k = len(nums)-1
            j = i + 1           
            while (j < k):
                
                _sum = nums[i] + nums[j] + nums[k]

                if _sum < 0:
                    j = j + 1
                    continue
                if _sum > 0:
                    k = k - 1
                    continue
                    
                row = [nums[i], nums[j], nums[k]]
                result.append(row)
                
                j = j + 1
                k = k - 1
                while j < len(nums) and nums[j] == nums[j-1]:
                    j = j + 1
                while k > j and nums[k] == nums[k+1]:
                    k = k - 1
            

        return result

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        sum_nums = [(item, item*count[item]) for item in count]
        sum_nums.sort()
        get = 0
        not_get = 0
        
        for i in range(len(sum_nums)):
            if (i-1>=0 and (sum_nums[i-1][0]+1 == sum_nums[i][0])):
                get, not_get = not_get + sum_nums[i][1], max(get,not_get)

            else:
                get, not_get = max(get,not_get) + sum_nums[i][1], max(get,not_get)
        
        return max(get,not_get)

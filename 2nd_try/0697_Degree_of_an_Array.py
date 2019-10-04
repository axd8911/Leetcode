class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        appear = collections.Counter(nums)
        most = max(appear.values())

        dic = collections.defaultdict(list)
        for i in range(len(nums)):
            dic[nums[i]].append(i)

        most_list = []
        for item in appear:
            if appear[item] == most:
                most_list.append(item)

        shortest = float('inf')
        for item in most_list:
            degree = dic[item][-1]-dic[item][0]+1
            shortest = min(degree,shortest)
        return shortest

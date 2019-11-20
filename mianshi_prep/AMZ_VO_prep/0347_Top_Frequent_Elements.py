class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = collections.Counter(nums)
        myHeap = [(-cnt[key],key) for key in cnt]
        heapq.heapify(myHeap)
        res = heapq.nsmallest(k,myHeap)
        return [item[1] for item in res]


# bucket search
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = collections.Counter(nums)

        bucket = [[] for i in range(len(nums)+1)]

        for key in dic:
            bucket[dic[key]].append(key)

        res = []
        for i in range(len(bucket)-1,-1,-1):
            if bucket[i]:
                for item in bucket[i]:
                    res.append(item)
                    if len(res)==k:
                        return res

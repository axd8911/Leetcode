class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = collections.Counter(tasks)
        maximum = max(cnt.values())
        freq = len([cnt[item] for item in cnt if cnt[item] ==maximum])
        return max((maximum-1)*(n+1) + freq,len(tasks))

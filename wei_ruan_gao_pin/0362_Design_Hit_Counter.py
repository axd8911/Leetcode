class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hits = []
        

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        if not self.hits or timestamp != self.hits[-1][0]:
            self.hits.append([timestamp,1])
        else:
            self.hits[-1][1]+=1        

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        l,r = 0,len(self.hits)-1
        start = len(self.hits)
        while l<=r:
            mid = (l+r)//2
            if self.hits[mid][0] > timestamp-300 and (mid==0 or self.hits[mid-1][0]<=timestamp-300):
                start = mid
            if self.hits[mid][0]>timestamp-300:
                r-=1
            else:
                l+=1
        l,r = 0,len(self.hits)-1
        end = -1
        while l<=r:
            mid = (l+r)//2
            if self.hits[mid][0]<=timestamp and (mid==len(self.hits)-1 or self.hits[mid+1][0]>timestamp):
                end = mid
            if self.hits[mid][0]<=timestamp:
                l+=1
            else:
                r-=1
        if start == len(self.hits) or end == -1:
            return 0
        else:
            return sum(item[1] for item in self.hits[start:end+1])
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)

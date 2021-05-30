class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dic:
            self.dic[key] = [[value],[timestamp]]
        else:
            idx = bisect.bisect(self.dic[key][1], timestamp)
            self.dic[key][0].insert(idx, value)
            self.dic[key][1].insert(idx, timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic:
            return ''
        allvalues,alltimes = self.dic[key]
        if timestamp>=alltimes[-1]:
            return allvalues[-1]
        if timestamp<alltimes[0]:
            return ''
        
        start,end = 0,len(allvalues)
        while start<=end:
            mid = (start+end)//2
            if timestamp<alltimes[mid]:
                end = mid-1
            else:
                start=mid+1
        return allvalues[end]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

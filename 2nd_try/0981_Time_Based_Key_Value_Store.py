class TimeMap:
    # binary search
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:

        elements = self.dic[key]
        l,r = 0,len(elements)-1
        if timestamp >= elements[r][0]:
            return elements[r][1]
        if timestamp < elements[l][0]:
            return ''

        while l<=r:
            mid = (l+r)//2
            if elements[mid][0] <= timestamp < elements[mid+1][0]:
                return elements[mid][1]
            if timestamp<elements[mid][0]:
                r = mid - 1
            else:
                l = mid + 1


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

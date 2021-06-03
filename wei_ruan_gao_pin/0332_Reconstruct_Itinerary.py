class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        dic = collections.defaultdict(list)
        for a,b in tickets:
            heapq.heappush(dic[a],b)
        print (dic)
        output = []
        
        def helper(location):
            while dic[location]:
                curr = heapq.heappop(dic[location])
                helper(curr)
            output.append(location)
        
        helper('JFK')

        return output[::-1]

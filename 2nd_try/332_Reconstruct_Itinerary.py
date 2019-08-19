class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        match = collections.defaultdict(list)
        for depart,arrive in tickets:
            heapq.heappush(match[depart],arrive)
        output = []
        def dfs(depart):
            while match[depart]:
                dfs(heapq.heappop(match[depart]))
            output.append(depart)
        dfs('JFK')
        return output[::-1]

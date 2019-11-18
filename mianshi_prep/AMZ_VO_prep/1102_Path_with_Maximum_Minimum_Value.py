class Solution:
    def maximumMinimumPath(self, A: List[List[int]]) -> int:

        # BFS and pq. each step the own path should update its minimum. Find the maximum of all the minimums
        # update the maximum in current step

        h = len(A)
        w = len(A[0])
        visited = {(0,0)}
        myheap = [[-A[0][0],0,0]]
        res = float('inf')

        while myheap:
            print (res,myheap)
            score,x0,y0 = heapq.heappop(myheap)
            # take the best one, opt it and move along
            res = min(res,-score)
            if (x0,y0)==(h-1,w-1):
                return res
            for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                x = x0+dx
                y = y0+dy
                if 0<=x<h and 0<=y<w and (x,y) not in visited:
                    print ([-A[x][y],x,y])
                    heapq.heappush(myheap,[-A[x][y],x,y])
                    visited.add((x,y))

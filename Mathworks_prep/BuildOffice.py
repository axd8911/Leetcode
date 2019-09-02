import collections
class Solution:
    def buildOffice(self,h,w,n):
        buildings = []
        def location(l,comb,n):
            if n == 0:
                buildings.append(comb[:])
                return
            for i in range(l-1,-1,-1):
                comb[i] = 1
                location(i,comb,n-1)
                comb[i] = 0
        l = w*h
        comb = [0 for _ in range(l)]
        location(l,comb,n)

        def convert(building):
            output = [[0 for _ in range(w)] for _ in range(h)]
            for i in range(h):
                for j in range(w):
                    output[i][j] = building[i*w+j]
            return output

        buildings = [convert(building) for building in buildings]
        # print(buildings)

        self.largest = float('inf')
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        def bfs(building):
            curr = collections.deque([])
            visited = set()
            distance = 0
            #print (h,w,building)
            for i in range(h):
                for j in range(w):
                    if building[i][j] == 1:
                        curr.append([i,j])
                        visited.add((i,j))
            while curr:
                distance += 1
                for i in range(len(curr)):
                    x,y = curr.popleft()
                    for dx,dy in directions:
                        if (x+dx,y+dy) not in visited and 0<=x+dx<h and 0<=y+dy<w:
                            visited.add((x+dx,y+dy))
                            curr.append([x+dx,y+dy])
            return distance-1

        for building in buildings:
            self.largest = min(self.largest, bfs(building))
        return self.largest


def main():
    a = Solution().buildOffice(4,7,3)
    print (a)

main()
